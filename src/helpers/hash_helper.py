from hashlib import md5
from zlib import adler32


def compute_md5(chunk):
    return md5(str_to_bytes(chunk)).hexdigest()


def compute_adler32(chunk):
    return adler32(str_to_bytes(chunk))


def str_to_bytes(string) -> bytes:
    return bytes(string, 'utf-8')
