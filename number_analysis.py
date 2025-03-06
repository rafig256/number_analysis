def prime_factors(n):
    factors = []
    # بررسی عدد 2 به طور جداگانه
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    
    # بررسی اعداد فرد
    divisor = 3
    while divisor * divisor <= n:
        while n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        divisor += 2  # فقط اعداد فرد را بررسی کنید

    # اگر عدد باقیمانده خود عدد اول باشد
    if n > 1:
        factors.append(n)

    return factors

# دریافت ورودی از کاربر
number = int(input("Enter a number to factorize: "))
if number <= 0:
    print("Please enter a positive integer greater than 1.")
else:
    result = prime_factors(number)
    if len(result) == 1:
        print ('عدد وارد شده یک عدد اول است')
    else:
        print(f"The prime factors of {number} are: {result}")