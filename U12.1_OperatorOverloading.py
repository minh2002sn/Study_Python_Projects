class Vector:
	def __new__(cls, *args, **kwargs):
		print('__new__() function is called.')
		instance = object.__new__(cls)
		return instance

	def __init__(self, x: float = 0.0, y: float = 0.0):
		print('__init__() function is called.')
		self.x = x
		self.y = y

	def __str__(self):
		return f'({self.x}, {self.y})'

	def __add__(self, v):
		x = self.x + v.x
		y = self.y + v.y
		instance = Vector(x, y)
		return instance

v1 = Vector(1.0, 2.0)
v2 = Vector(3.0, 4.0)
print(v1+v2)