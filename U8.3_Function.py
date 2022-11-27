def sum(start, *args):
	for n in args:
		start += n
	return start

print(sum(0, 1, 2))
print(sum(2, 5))
print(sum(2, 4, 6, 8, 10))