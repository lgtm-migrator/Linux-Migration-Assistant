from typing import List

from backups.chunks import Chunk, Signature
from .hash_helper import compute_adler32

from pathlib import Path

BLOCK_SIZE = 4096


def checksums_file(file_path: Path):
    chunks = Chunk()
    with open(file_path) as f:
        while True:
            chunk = f.read(BLOCK_SIZE)
            if not chunk:
                break
            chunks.append(
                Signature(
                    adler32=compute_adler32(chunk),
                )
            )
    return chunks


def get_different_blocks(src: str, dst: str) -> List[int]:
    checksum_src = checksums_file(file_path=src)
    checksum_dst = checksums_file(file_path=dst)
    different_blocks = []
    with open(src) as f:
        while True:
            chunk = f.read(BLOCK_SIZE)
            if not chunk:
                break

            chunk_block = checksum_dst.get_chunk(chunk=chunk)
            if chunk_block is None:
                different_blocks.append(checksum_src.get_chunk(chunk=chunk))

    return different_blocks
