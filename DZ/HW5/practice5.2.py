l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
L = []
a = 0
for i in l:
    for n in range(2, i):
        if not i % n:
            a += 1
    if a == 0:
        L.append(i)
    else:
        a = 0
def square(m):
    return m**2
squared_numbers = list(map(square, L))
print(squared_numbers)