num = int(input("Enter a number: "))

square = num * num

temp = num

while temp > 0:
    if temp % 10 != square % 10:
        print(num, "is Not an Automorphic Number")
        break

    temp = temp // 10
    square = square // 10

else:
    print(num, "is an Automorphic Number")
