def evenNum(res):
    ans = []
    for i in res:
        if(i % 2 == 0):
            ans.append(i)
    print(ans)

#Initial list
res = []

# Input lengths
lengths = int(input())

# Add element
for i in range(lengths):
    # Input elements
    n = int(input())
    res.append(n)
evenNum(res)