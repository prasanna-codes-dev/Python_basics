def armstrong(num):
    original = num
    total = 0

    while num > 0:
        digit = num % 10
        total = total + (digit ** 3)
        num = num // 10

    return total == original


number = int(input("Enter a number: "))

if armstrong(number):
    print(number, "is an Armstrong Number")
else:
    print(number, "is Not an Armstrong Number")
