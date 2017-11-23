# -*- coding: utf-8 -*-

class Base:
    # クラス直下に定義した変数はクラス変数
    __attr = 100

    # constucot(selfという引数が必ず必要になるようです。それ以外にも引数をつけることも可能です)
    def __init__(self, num):
        print('called constructor')
        self.__attr = num

    # 
    def method(self):
        print('called public method')
        self.__method()

    # __を付与するとprivateとして扱われます
    def __method(self):
        print('called private method')
        print(self.__attr)

    # __del__はdestructorとして扱われるようですが、仕様上は呼ばれないことなどもあるようです。
    def __del__(self):
        print('called destructor')

base = Base(100)
base.method()   #OK
#base.__method() #NG(error)
