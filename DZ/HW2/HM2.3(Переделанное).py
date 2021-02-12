fizz = int(input())
buzz = int(input())
a = int(input())
k = range(1, a+1)
list = []
for m in k:
    if m % fizz == 0 and m % buzz == 0:
        list.append("FB")
    elif m % fizz == 0:
        list.append("F")
    elif m % buzz == 0:
        list.append("B")
    else:
        list.append(m)
print(list)

