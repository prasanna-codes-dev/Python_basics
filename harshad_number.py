num = int(input("Enter a number: "))

temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    sum = sum + digit
    temp = temp // 10

if num % sum == 0:
    print(num, "is a Harshad Number")
else:
    print(num, "is Not a Harshad Number")
