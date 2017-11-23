# 概要
クラスを使ったブレークポイントの貼り方について

# 詳細

次のようにSuperClassというクラスを処理する手前の場合には、まだブレークポイントを貼ることが出来ない。
```
$ python -m pdb test.py 
> /home/tsuyoshi/git/python/pdb/ClassSample/test.py(4)<module>()
-> class SuperClass(object):    #classの宣言
(Pdb) list
  1  	#! /usr/bin/env python 
  2  	# -*- coding: utf-8 -*- 
  3  	
  4  ->	class SuperClass(object):    #classの宣言
  5  	    name = ''
  6  	    __callcount = 0 #private変数
  7  	
  8  	    def __init__( self ): #コンストラクタ
  9  	        self.name = 'SuperClass' 
 10  	
 11  	    def call( self ): #メソッドのself記述の省略はできません。ちょっと面倒です。 
(Pdb) b SuperClass.call
*** The specified object 'SuperClass.call' is not a function
or was not found along sys.path.
```

しかし、該当クラスを超えるとブレークポイントを引っ掛けることができるようになります。
```
(Pdb) n
> /home/tsuyoshi/git/python/pdb/ClassSample/test.py(39)<module>()
-> if __name__ == '__main__' :
(Pdb) b SuperClass.call
Breakpoint 1 at /home/tsuyoshi/git/python/pdb/ClassSample/test.py:11
(Pdb) c
> /home/tsuyoshi/git/python/pdb/ClassSample/test.py(12)call()
-> self.__callcount = self.__callcount + 1
(Pdb) list
  7  	
  8  	    def __init__( self ): #コンストラクタ
  9  	        self.name = 'SuperClass' 
 10  	
 11 B	    def call( self ): #メソッドのself記述の省略はできません。ちょっと面倒です。 
 12  ->	        self.__callcount = self.__callcount + 1
 13  	        return self.name 
 14  	
 15  	    def getCallCount( self ):
 16  	        return self.__callcount 
 17  	
```


# 参考URL
- how to make a breakpoint on class member function of python？ [duplicate]
  - https://stackoverflow.com/questions/8221040/how-to-make-a-breakpoint-on-class-member-function-of-python
