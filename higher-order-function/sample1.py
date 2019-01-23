#!/usr/bin/python3

# reduce関数利用に必須
from functools import reduce

# 組み込み関数(map)
#   iterableを引数として受け取り、各要素に対して関数を適用する。
#   map( 関数, iterable )
print("Using map function")
lst = [-1, 3, -5, 7, -9] 
print( list( map(abs, lst) )) 
 

# map + ラムダ式 
#   iterableを引数として受け取り、各要素をlambdaの後に定義して処理を記述する。
print("\nUsing map + lambda function")
lst = [-1, 3, -5, 7, -9] 
print ( list(map(lambda x: abs(x) * 2, lst) )) 
 

# 数値でフィルタリング(filter)
print("\nUsing filter + lambda function")
print (list (filter((lambda x: x < 0), range(-5,5))))


# リストを比較してフィルタリング(filter):  
# 2つのリストから一致したリストを出力する
print("\nUsing filter + lambda function to get matched number")
a = [1,2,3,5,7,9]
b = [2,3,5,6,7,8]
print (list(filter(lambda x: x in a, b)))


# product関数
#   複数のイテレータを取得して、すべての組み合わせに対してタプルを生成する。
print("\nUsing itertools.product")
import itertools 
lstA = [-1, 3, -5, 7] 
lstB = [2, 3] 
print( list(itertools.product(lstA, lstB) ))


# reduce関数 sample1
print("\nUsing itertools.product")
L = [1,2,3,4,5,6,7,8,9,10]
print (reduce(lambda a,b: a+b, L)) 

# reduce関数 sample2
print (reduce(list.__add__, [[1, 2, 3], [4, 5], [6, 7, 8]], []))

