#!/usr/bin/python3
# coding: utf-8

# このプログラム
#   普通に記述した場合とそれ以外の高階関数などを使って記述した場合の違いを確認するためのサンプル

from functools import reduce
# document
#   https://docs.python.jp/3/library/functools.html#functools.reduce

L = [1,2,3,4,5]

###############################
# Case1: 合計
###############################
print ("Case1")
# 普通に記述する場合
result = 0
for e in L:
    result += e
print (result)

# reduceを使う場合
print (reduce(lambda a,b: a+b, L))


###############################
# Case2: 総乗
###############################
print ("\nCase2: 総乗")

# 普通に記述する場合
result = L[0]
for e in L[1:]:
    result *= e
print (result)

# reduceを使う場合は次の通り
print (reduce(lambda a,b: a*b, L))


###############################
# Case3: リスト要素への演算処理
###############################
print ("\nCase3: リスト要素への演算処理")

# 普通に記述する場合
result = []
for e in L:
    result += [e*2]
print (result)

# reduceを使う場合
print (reduce(lambda a,b: a+[b*2], L, []))
print (reduce(lambda a,b: a+[b*2], L, [9,99,999]))   # 処理の違いを確認する参考までに9, 99, 999を入れている

# mapを使う場合
print (list(map(lambda x: x*2, L)))

# list内包表記を使う場合
print ([x*2 for x in L])

###############################
# Case4: 特定の数値によるフィルタリング処理を行う
###############################
print ("\nCase4: フィルタリング処理を行う")

# 普通に記述する場合
result = []
for e in L:
    if e > 3:
        result += [e]
print (result)

# フィルタリングの場合にはmapではなくfilterを利用する
print (reduce(lambda a,b: a+[b] if b > 3 else [], L, []))
print (list(filter(lambda x: x>3, L)))
print ([x for x in L if x > 3])

###############################
# Case5: 条件を絞ってから、要素に対して処理を適用する
###############################
print ("\nCase5: 条件を絞ってから、要素に対して処理を適用する")

# 普通に記述する場合
result = []
for e in L:
    if e > 3:
        result += [e*2]
print (result)

# reduceを使う場合 
print (reduce(lambda a,b: a+[b*2] if b > 3 else [], L, []))

# mapとfilterを組み合わせる場合
print (list(map(lambda x: x*2, filter(lambda x: x > 3, L))))

# リスト内包表記を使う場合
print ([x*2 for x in L if x > 3])






