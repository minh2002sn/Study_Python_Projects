from functools import reduce

def im_fact(n: int):
	p = 1
	for i in range(1, n+1):
		p *= i
	return p

def fun_fact(n: int):
	def mult(x, y): return x * y
	return reduce(mult, range(1, n+1))

def test1():
	n = 5
	f = im_fact(n)
	print(f'{n}! = {f}')

def test2():
	n = 5
	f = fun_fact(n)
	print(f'{n}! = {f}')

test1()
test2()