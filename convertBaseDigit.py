#!/usr/bin/python
# -*- coding: utf-8 -*-

# formatを利用した型変換について。パケット生成のためのゼロパディングなども可能

binary_number = 0b1010 # 2進数
octet_number = 0o700   # 8進数 (prefixは「0o」でも良い)
hex_number = 0xaaa     # 16進数

# スペース詰め(bなので2進数)
print "\n===スペース詰め(bなので2進数表記)"
print "{0:10b}".format(binary_number)
print "{0:10b}".format(octet_number)
print "{0:10b}".format(hex_number)

# スペース詰め(bなので2進数)
print "\n===スペース詰め(oなので8進数表記)"
print "{0:10o}".format(binary_number)
print "{0:10o}".format(octet_number)
print "{0:10o}".format(hex_number)

# スペース詰め (dなので10進数)
print "\n===スペース詰め(dなので10進数表記)"
print "{0:5d}".format(binary_number)
print "{0:5d}".format(octet_number)
print "{0:5d}".format(hex_number)

# ゼロ詰め (Xなので16進数)
print "\n===ゼロ詰め (Xなので16進数)"
print "{0:05X}".format(binary_number)
print "{0:05X}".format(octet_number)
print "{0:05X}".format(hex_number)

# 動的に埋める場合
print "\n===動的format"
print "{1:0{0}X}".format(5, 10)              # 下記と同じ意味
print "{val:0{len}X}".format(len=5, val=10)  # こちらは名前付き書式



