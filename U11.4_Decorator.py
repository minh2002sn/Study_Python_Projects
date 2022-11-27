def display_decorator(func):
	def wrapper(str):
		print(f'Log: The function {func.__name__} is executing...')
		func(str)
		print(f'Log: Execution completed.\n')
	return wrapper

def display(str):
	print(str)

displaying = display_decorator(display)
displaying('Hello World')

@display_decorator
def say_hello(str):
	print(str)

say_hello('Hello, Donald Trump')