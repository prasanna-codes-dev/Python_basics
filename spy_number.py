num = int(input("Enter a number: "))

temp = num
sum = 0
product = 1

while temp > 0:
    digit = temp % 10
    sum = sum + digit
    product = product * digit
    temp = temp // 10

if sum == product:
    print(num, "is a Spy Number")
else:
    print(num, "is Not a Spy Number")
