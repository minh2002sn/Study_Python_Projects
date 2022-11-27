class Person:
	# Class attribute
	MALE = True
	FEMALE = False
	count = 0

	# Constructor
	def __init__(self, fname: str = "",
						lname: str = "",
						age: int = 0,
						gender: bool = 1):
		self.__fname = fname
		self.__lname = lname
		self.__age = age
		self.__gender = gender
		Person.count += 1
		self.__id = Person.count

	# Intance method
	def printInfo(self):
		print("ID: " + str(self.__id))
		print("Name: " + self.name)
		print("Age: " + str(self.age))
		print("Gender: " + "Male" if self.__gender else "Female")

	# Class Method
	@classmethod
	def showCount(cls):
		if cls.count > 1:
			print("There are " + str(cls.count) + " people.")
		else:
			print("There is " + str(cls.count) + " person.")

	# Property methed
	# Cách 1:
	@property
	def firstName(self):
		return self.__fname

	@firstName.setter
	def firstName(self, fname: str):
		if fname.isalpha():
			self.__fname = fname

	@property
	def lastName(self):
		return self.__lname

	@lastName.setter
	def lastName(self, lname):
		if lname.isalpha():
			self.__lname = lname

	# Cách 2:
	def getAge(self):
		return self.__age

	def setAge(self, age):
		if age > 0:
			self.__age = age

	def getGender(self):
		return self.__gender

	def setGender(self, gender):
		self.__gender = gender

	def getName(self):
		return self.__fname + " " + self.__lname

	age = property(getAge, setAge)
	gender = property(getGender, setGender)
	name = property(getName)






class Student(Person):
	# Contrucstor
	def __init__(self, fname: str = "",
						lname: str = "",
						age: int = 0,
						gender: bool = 1,
						grade: int = 1,
						mark: float = 0.0):
		super().__init__(fname, lname, age, gender)	# Overriding
		self.__grade = grade
		self.__mark = mark

	# Intance method
	def printInfo(self):
		super().printInfo()	# Overriding
		print("Grade: " + str(self.__grade))
		print("Mark " + str(self.__mark))