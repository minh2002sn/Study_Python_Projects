n = int(input())
lst1 = []
lst2 = []
for i in range(n):
    lst1.append(int(input()))
    if lst1[i] % 5 == 0:
        lst2.append(lst1[i])
if len(lst2) == 0:
    lst2.append(0)
    print(lst2)
else:
    print(lst2)