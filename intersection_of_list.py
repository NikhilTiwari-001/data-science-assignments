a = [1, 2, 3]
b = [2, 3, 4]
intersection = []
for i in a:
    if i in b and i not in intersection:
        intersection.append(i)
print(intersection)
