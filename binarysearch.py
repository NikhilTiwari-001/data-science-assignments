lst = [1, 3, 5, 7, 9]
target = 5
low = 0
high = len(lst) - 1
found = False
while low <= high:
    mid = (low + high) // 2
    if lst[mid] == target:
        found = True
        break
    elif lst[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
if found:
    print("Found")
else:
    print("Not Found")
