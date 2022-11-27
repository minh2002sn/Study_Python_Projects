class Person:
	def __init__(self, name, age: int = 1):
		self.name = name
		self.age = age

	def printInfor(self):
		print(f'{self.name} ({self.age} years old)')

	@staticmethod
	def elder(person):
		if person.age >= 75:
			return True
		return False

teacher = [Person('A', 25), Person('B', 30), Person('C', 75), Person('D', 80), Person('E', 35)]

old_teacher = filter(Person.elder, teacher)
for p in old_teacher:
	p.printInfor()