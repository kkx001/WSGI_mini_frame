def  line(k,b):
	def create_y(x):
		print(k * x + b)
	
	return create_y

line_1 = line(2,1)
line_1(0)
line_1(1)
line_1(2)


# 思考：函数、匿名函数、闭包、对象 当做实参时 有什么区别？
# 1. 匿名函数能够完成基本的简单功能，，，传递是这个函数的引用 只有功能
# 2. 普通函数能够完成较为复杂的功能，，，传递是这个函数的引用 只有功能
# 3. 闭包能够将较为复杂的功能，，，传递是这个闭包中的函数以及数据，因此传递是功能+数据
# 4. 对象能够完成最为复杂的功能，，，传递是很多数据+很多功能，因此传递是功能+数据
# 

#修改闭包中的数据

x = 300
def test_1():
	x=200
	def test_2():
		nonlocal x   当有nonlocal时，可以修改x的值
		print("x = %s" %x)

		x = 100
		print("x = %s" %x)
	return test_2

t = test_1()
t()