import logging
from collections import namedtuple
from typing import Optional

from helpers.hash_helper import compute_adler32

logger = logging.getLogger(f'migration_assistant_{__name__}')

Signature = namedtuple('Signature', {'adler32'})


class Chunk:
    """
    Data structure to hold rolling checksum
    """
    def __init__(self):
        self._chunks = []
        self._chunk_signature = {}

    def append(self, signature: Signature) -> None:
        self._chunks.append(signature)
        self._chunk_signature[signature.adler32] = len(self._chunks) - 1

    def get_chunk(self, chunk: bytes) -> Optional[int]:
        try:
            return self._chunk_signature[compute_adler32(chunk)]
        except KeyError:
            logger.info('Chunk not found')
            return None

    def __getitem__(self, index_signature: Signature) -> int:
        return self._chunks[index_signature]

    def __len__(self):
        return len(self._chunks)
