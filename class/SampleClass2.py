# -*- coding: utf-8 -*-

# クラスメソッドとスタティックメソッドの定義方法を確認する@マークによるデコレータという仕組みを利用する

class Base:
    __attr = 100

    def __init__(self, num):
        print('called constructor')
        self.__attr = num

    # クラスメソッドの定義
    @classmethod
    def class_method(cls):                 # クラスメソッドではclsと呼ぶようです
        print('called public classmethod')

    # スタティックメソッドの定義
    @staticmethod
    def static_method(self):
        print('called public staticmethod')

    def __del__(self):
        print('called destructor')


# スタティックメソッドの呼び出し
Base.static_method(10)

# クラスメソッドの呼び出し
base = Base(100)
base.class_method()
