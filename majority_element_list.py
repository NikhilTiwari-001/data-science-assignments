lst = [1, 2, 2, 2, 3, 2]
for i in lst:
    if lst.count(i) > len(lst) // 2:
        print("Majority Element:", i)
        break
else:
    print("No Majority Element")
