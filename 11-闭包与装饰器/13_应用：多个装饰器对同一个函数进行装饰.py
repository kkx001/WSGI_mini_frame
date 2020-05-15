def set_func1(func):
	def call_func():
		return "<h1>" +func() + "</h1>"

	return call_func

def set_func2(func):
	def call_func():
		return "<td>" + func() + "</td>"
	return call_func

@set_func1
@set_func2
def test():
	return "hahaha"

print(test())