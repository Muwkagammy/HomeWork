digits = list(range(1,101))
print(digits)
i = 0
while i < len(digits):
    digit = digits[i]
    if 5 <= digit <= 19:
        print(digit, "Процентов")
    else:
        result = digit % 10
        if result == 1:
            print(digit, "Процент")
        elif 2 <= result <= 4:
            print(digit, "Процента")
        elif 5 <= result <= 9 or result == 0:
            print(digit, "Процентов")
    i += 1


