lst = [5, 10, 15]
target = 10
found = False
for i in lst:
    if i == target:
        found = True
        break
if found:
    print("Found")
else:
    print("Not Found")
