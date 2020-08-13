from backups.chunks import Chunk, Signature
from .hash_helper import compute_md5, compute_adler32

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
                    md5=compute_md5(chunk),
                )
            )
    return chunks


def has_different_blocks(src, dst):
    is_different = True
    checksum_file_two = checksums_file(dst)
    with open(src) as f:
        while True:
            chunk = f.read(BLOCK_SIZE)
            if not chunk:
                break

            if checksum_file_two.get_chunk(chunk=chunk) is None:
                return is_different
    return not is_different
