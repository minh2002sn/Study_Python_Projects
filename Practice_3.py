str = str(input())

def check(s):
    a = s.split(" ")
    ans = []
    for i in range(len(a)):
        if len(a[i]) > 3:
            ans.append(a[i])
    print(ans)

check(str)