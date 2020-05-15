def set_func1(func):
	print("---开始进行装饰权限1的功能---")
	def call_func(*args, **kwargs):
		print("---这是权限验证1----")
		return func(*args, **kwargs)

	return call_func


def set_func2(func):
	print("---开始进行装饰权限2的功能---")
	def call_func(*args, **kwargs):
		print("---这是xxx的功能----")
		return func(*args, **kwargs)

	return call_func


@set_func1
@set_func2
def test(num, *args, **kwargs):
	print("---test---%d" %num)
	print("---test---", args)
	print("---test---", kwargs)

test(100,200,300)
