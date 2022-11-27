age = int(input())

print("Your cat is young") if age < 5 else print("Your cat is old")

if age < 5:
	print("Your cat is young")
elif age < 7:
	print("Your cat is old")
else:
	print("Your cat is very old")