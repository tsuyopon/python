#!/usr/bin/env python3
#
# 以下のテストベクターをチェックする簡単なテスト
# https://tools.ietf.org/html/rfc5869#appendix-A.1
#
import hashlib
import binascii
import hmac
from math import ceil
from binascii import hexlify, unhexlify

# SHA256 = ハッシュの長さ32byte
hash_len = 32

def hmac_sha256(key, data):
    return hmac.new(key, data, hashlib.sha256).digest()

# ikm = input key material
def hkdf(length, ikm, salt, info):
    prk = hmac_sha256(salt, ikm)
    print (hexlify(prk))
    t = b""
    okm = b""
    for i in range(ceil(length / hash_len)):
        t = hmac_sha256(prk, t + info + bytes([1+i]))
        okm += t
    return okm[:length]


ikm  = unhexlify("0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b")
salt = unhexlify("000102030405060708090a0b0c")
info = unhexlify("f0f1f2f3f4f5f6f7f8f9")
L = 42

print (hexlify(hkdf(L, ikm, salt, info)))

