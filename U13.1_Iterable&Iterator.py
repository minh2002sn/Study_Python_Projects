class FibonacciIterable:
	def __init__(self, count = 10):
		self.count = count

	def __iter__(self):
		return FibonacciIterator(self.count)

class FibonacciIterator:
	def __init__(self, count = 10):
		self.a, self.b = 0, 1
		self.count = count
		self.__i = 0

	def __next__(self):
		if self.__i > self.count:
			raise StopIteration()
		value = self.a
		self.a, self.b = self.b, self.a + self.b
		self.__i += 1
		return value

def test1():
	print('Test 1:', end=' ')
	iterable = FibonacciIterable(5)
	for f in iterable:
		print(f, end=' ')
	print()

def test2():
	print('Test 2:', end=' ')
	try:
		iterator = FibonacciIterator(5)
		for f in iterator:
			print(f, end=' ')
		print()
	except:
		print('[ERROR]')

def test3():
	print('Test 3:', end=' ')
	iterator = FibonacciIterator(5)
	while True:
		try:
			f = next(iterator)
			print(f, end=' ')
		except StopIteration:
			break
	print()

def test4():
	print('Test 4:', end=' ')
	iterable = FibonacciIterable(5)
	iterator = iter(iterable)
	while True:
		try:
			f = next(iterator)
			print(f, end=' ')
		except StopIteration:
			break
	print()

test1()
test2() #Error
test3()
test4()