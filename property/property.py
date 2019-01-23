#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 Pythonのpropertyのサンプルについて
 参考URL: http://nametake-1009.hatenablog.com/entry/2015/10/21/222829

 @propertyでgetterを表す。@function.setterでsetterを表す。
"""



class Image(object):

	def __init__(self):
		self._width = 300
		self._height = 400

	# width関数が2つ定義されている。@propertyの方がgetterとなる
	@property
	def width(self):
		print("@property width function")
		return self._width

	@width.setter
	def width(self, width):
		print("@width.setter function")
		self._width = width

	# height関数が2つ定義されている。@propertyの方がgetterとなる
	@property
	def height(self):
		print("@property height function")
		return self._height

	@height.setter
	def height(self, height):
		print("@height.setter function")
		self._height = height

if __name__ == '__main__':
	img = Image()

	print("[__main__] set img.width")
	# @propertyのwidthを呼び出す
	img.width = 200
	print("[__main__] set img.height")
	img.height = 100
	print(img.width)
	print(img.height)
