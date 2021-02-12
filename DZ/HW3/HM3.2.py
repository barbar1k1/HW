file = open("hw3.2(numbers).txt", 'r')
S = []
for i in file:
    n = list(map(int,i.split()))
    fizz = n[0]
    buzz = n[1]
    l = n[2]
    for e in range(1, l + 1):
        if e % fizz == 0 and e % buzz == 0:
            S.append("FB")
        elif e % fizz == 0:
            S.append("F")
        elif e % buzz == 0:
            S.append("B")
        if e % fizz and e % buzz:
            S.append(e)
print(S)
file.close()
file1 = open("hw3.3(numbers).txt", 'a')
file1.write(str(S))
file1.close()
