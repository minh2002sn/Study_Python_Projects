class Book:
	# Class attribute
	count  = 0

	# Constructor
	def __init__(self, title: str = "", authors: str = "", year: int = 0):
		Book.count += 1
		self._id = Book.count		# Protected attribute
		self.__title = title		# Private attribute
		self.authors = authors		# Public attribute
		self.year = year			# Public attribute

	# Instance method
	def printInfo(self):
		print("ID: " + str(self._id))
		print("Book's name: " + self.__title)
		print("Writen by " + self.authors + " in " + str(self.year))

	# Class Method
	@classmethod
	def showCount(cls):
		if cls.count > 1:
			print("There are " + str(cls.count) + " books.")
		else:
			print("There is " + str(cls.count) + " book.")