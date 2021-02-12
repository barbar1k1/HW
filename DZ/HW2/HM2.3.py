fizz = int(input())
buzz = int(input())
a = int(input())
k = range(1, a)
for m in k:
    if m % fizz == 0:
        print("F")
    if m % buzz == 0:
        print("B")
    if m % fizz and m % buzz:
        print(m)