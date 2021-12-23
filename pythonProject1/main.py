s, p = map(int, input().split())
count = 0
a = 1
b = a
c = b

while a + b + c <= s and a * b * c <= p and a < p + 1 and b < p + 1 and c < p + 1:
    a += 1
    b += 1
    c += 1
    count += 1


print(count)

