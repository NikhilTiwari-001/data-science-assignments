num = 153
digits = len(str(num))
if num == sum(int(d)**digits for d in str(num)):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
