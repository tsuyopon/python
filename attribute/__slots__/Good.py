class Test(object):
	__slots__ = ['isSuccess']
	def  __init__ (self):
		self.isSuccess = False;

	# 変数名isSuccessのスペルミスをした場合には、本来はエラーにしてほしい
	def setSuccess(self):
		self.isSuccccccess = True;

	def printIsSuccess(self):
		print(self.isSuccess);

t =Test();
t.printIsSuccess();
t.setSuccess();
t.printIsSuccess();
