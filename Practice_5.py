s = str(input())

def format(str):
    if len(str) > 3:
        if str[-3:] == "ing":
            str += "ly"
        else:
            str += "ing"
    print(str)

format(s)