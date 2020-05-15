
class Test(object):
	"""docstring for Test"""
	def __init__(self,func):
		self.func = func

	def __call__(self):
		print("这里是装饰器添加的功能.....")
		return self.func()

@Test
def test():
	return "hahaha"

print(test())

