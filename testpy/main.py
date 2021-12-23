s, p = map(int, input().split())
count = 0
for a in range(1, p + 1):
    for b in range(1, p + 1):
        for c in range(1, p + 1):
            if a + b + c <= s and a * b * c <= p:
                count +=1
print(count)