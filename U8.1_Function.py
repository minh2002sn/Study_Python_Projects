def sum_of_list(lst):
    s = 0
    for i in lst:
        s += i
    return s

n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
print(sum_of_list(lst))