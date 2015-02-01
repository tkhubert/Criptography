__author__ = 'tkhubert'

import numpy as np
from Crypto.Cipher import AES
from Crypto.Hash   import SHA256
from binascii import hexlify, unhexlify

def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

def hexxor(a, b):
    return hexlify(strxor(unhexlify(a), unhexlify(b)))