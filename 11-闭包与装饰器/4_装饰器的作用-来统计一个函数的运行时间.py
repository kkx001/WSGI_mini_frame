import time


def set_func(func):
	def call_func():
		start_time = time.time()
		func()
		stop_time = time.time()

		print("alltimeis %f" % (stop_time - start_time))
	return call_func

@set_func
def test1():
	print("-----test1-----")
	for i in range(1000):
		pass

test1()

test1()
