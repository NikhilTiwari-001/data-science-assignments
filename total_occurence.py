lst = [1, 2, 2, 3, 1, 4]
counts = {}
for item in lst:
    if item in counts:
        counts[item] += 1
    else:
        counts[item] = 1
print(counts)
