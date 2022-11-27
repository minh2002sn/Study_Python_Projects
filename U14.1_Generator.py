class FibonaccyIterable:
	def __init__(self, count = 10):
		self.a, self.b = 0, 1
		self.count = count

	def __iter__(self):
		i = 0
		while True:
			if i > self.count:
				break
			yield self.a
			self.a, self.b = self.b, self.a + self.b
			i += 1

def test1():
	iterable = FibonaccyIterable(5)
	for i in iterable:
		print(i, end = ' 	')

test1()