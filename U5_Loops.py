n = int(input())
s = 0
for i in range(1, n+1):
	s += i
print(s)

s = 0
j = 1
while j <= n:
	s += j
	j += 1
print(s)