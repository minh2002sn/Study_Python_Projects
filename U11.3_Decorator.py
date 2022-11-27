def welcome(greeting: str = 'Hi'):
	def hello(name: str = 'Nguyen Van A'):	#Closure
		print(f'{greeting}, {name}. Wellcome to heaven!')
	return hello

otherName0 = welcome()
otherName1 = welcome()
otherName2 = welcome('Hello')

otherName0()
otherName1('Obama')
otherName2('Trump')