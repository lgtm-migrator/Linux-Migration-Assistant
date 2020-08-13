from hashlib import md5
from zlib import adler32

BLOCK_SIZE = 4096


def compute_md5(chunk):
    return md5(chunk).hexdigest()


def compute_adler32(chunk):
    return adler32(chunk)


