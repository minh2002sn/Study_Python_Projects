def ex1():
	i = 10
	yield i + 10
	yield i - 10
	yield i * 10
	yield i / 10

for value in ex1():
	print(value, end = ' ')