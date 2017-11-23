# -*- coding: utf-8 -*-

# 継承について

# 基底クラスの定義
class BaseClass(object):

    def __init__(self, a, b):
        print('called BaseClass constructor')
        self.a = a
        self.b = b

    def sum(self):
        print('called sum function')
        return self.a + self.b

# 派生クラスの定義。class宣言のカッコ内には基底クラスを宣言する
class DerivedClass(BaseClass):

    def __init__(self, a, b):
        print('called DerivedClass constructor')
        super(DerivedClass, self).__init__(a, b)

        # スーパークラスのメソッドもここで使える
        print('called BaseClass.sum() from DerivedClass')
        print self.sum()

if __name__ == '__main__':

    cls = DerivedClass(10, 5)
    print "sum:" + str(cls.sum())
    print "a:" + str(cls.a)
    print "b:" + str(cls.b)

