a = int(input())
b = int(input())

def gcd(a,b):
    if a == b:
        print(a);
    else:
        ans = 1;
        while a != b:
            if a > b:
                a -= b
            if b > a:
                b -= a
            if a == b:
                ans = a
        print(ans)

gcd(a, b)