def foo(**kwargs):
	for key, value in kwargs.items():
		print(key + " = " + str(value))

foo(a = 1, b = 2, c = 3)