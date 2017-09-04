#!/usr/bin/python
# -*- coding: utf-8 -*-

# 型の変換について


print hex(65)             # '0x41' 16進数文字列へ変換
print oct(65)             # '0101' 8進数文字列へ変換
print bin(65)             # '0b1000001' 2進数文字列へ変換
print format(0x41,'b')    # '1000001'
print format(0x41,'16b')  # '1000001'
print format(0x41,'016b') # '1000001'
print int('41',16)        # 65 16進数文字列を数値へ変換
print int('65')           # 65 10進数文字列を数値へ変換
print int('1000001',2)    # 65
print int('0xffff', 16)   # 16進数へ変換
print str(6565)           # '6565' 1byte以上の数値を10進数文字列へ変換
print chr(65)             # 'A' 数値をASCII文字へ変換
print ord('A')            # 65 ASCII文字を数値へ変換

print "percent"
print '%o' % 8
print '%06o' % 8
