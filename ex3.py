a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new = []

for each in a:
    if each < 10:
        new.append(each)
print(new)

print([x for x in a if x < 10])

another = a[:]
print(another)