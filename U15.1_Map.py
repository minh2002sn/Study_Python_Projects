X = [x/100 for x in range(100, 500, 100)]

def parabolic(x, a = 1.0, b = 0.0, c = 0.0):
	return a*x*x + b*x + c

#Cách 1:
Y1 = []
for x in X:
	y = parabolic(x)
	Y1.append(y)
for y in Y1:
	print(y, end = ' ')
print()

#Cách 2
Y2 = list(map(parabolic, X))
for y in Y2:
	print(y, end = ' ')
print()