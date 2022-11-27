#Initial list
res = []

# Input lengths
lengths = int(input())
s = ""
# Add element
for i in range(lengths):
    # Input elements
    n = int(input())
    res.append(n)
    s += str(n)
print(s)