def hello(name):
	print(f'Hello, {name}. Wellcome to heaven!')

def hi(name):
	print(f'Hi, {name}. Wellcome to hell!')

#High order function
def greeting(name, func):
	print('Inside high order function:')
	print('========== Star ==========')
	func(name)
	print('========== Stop ==========')
	print()

greeting('Donald Trump', hello)
greeting('Vladimir Putin', hi)