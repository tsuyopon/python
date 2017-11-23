# -*- coding: utf-8 -*-

# 多重継承に関するサンプル

class A(object):
    def __init__(self):
        print 'Initialize A.'

    def method(self):
        print 'Call A method.'

class B(object):
    def __init__(self):
        print 'Initialize B.'

    def method(self):
        print 'Call B method.'

class C(object):
    def __init__(self):
        print 'Initialize C.'

    def method(self):
        print 'Call C method.'


class Main(A, B, C):
    def __init__(self):
        print('Initialize Main.')
        super(Main, self).__init__()
        super(A, self).__init__()
        super(B, self).__init__()
        
    def method(self):
        print('Call Main method')
        super(Main, self).method()
        super(A, self).method()
        super(B, self).method()
        
m = Main()
m.method()  
