for num in range(100, 1000):
    sum_of_digits = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum_of_digits += digit ** 3
        temp //= 10
    if num == sum_of_digits:
        print(num)
