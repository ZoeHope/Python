

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
num4 = int(input("Enter the fourth number: "))
num5 = int(input("Enter the fifth number: "))


if (num1 == num2 or num1 == num3 or num1 == num4 or num1 == num5):
    print("DUPLICATES!")
elif (num2 == num3 or num2 == num4 or num2 == num5):
    print("DUPLICATES!")
elif (num3 == num4 or num3 == num5):
    print("DUPLICATES!")
elif(num4 == num5):
    print("DUPLICATES!")
else:
    print("ALL UNIQUE")
