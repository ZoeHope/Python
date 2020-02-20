

array_limit = 5
array = []

for index in range(array_limit):
    user_input = int(input("Please enter a number: "))
    array.append(user_input)

print(array)
array.sort()
print(array[0], " is the minimum.")
print(array[4], " is the maximum.")




def max_num(num1,num2,num3,num4,num5):
    if (num1 >= num2 and num1 >= num3 and num1 >= num4 and num1 >= num5):
        return num1
    elif (num2 >= num1 and num2 >= num3 and num2 >= num4 and num2 >= num5):
        return num2
    elif (num3 >= num1 and num3 >= num2 and num3 >= num4 and num3 >= num5):
        return num3
    elif (num4 >= num1 and num4 >= num2 and num4 >= num3 and num4 >= num5):
        return num4
    else:
        return num5


def min_num(num1,num2,num3,num4,num5):
    if (num1 <= num2 and num1 <= num3 and num1 <= num4 and num1 <= num5):
        return num1
    elif (num2 <= num1 and num2 <= num3 and num2 <= num4 and num2 <= num5):
        return num2
    elif (num3 <= num1 and num3 <= num2 and num3 <= num4 and num4 <= num5):
        return num3
    elif (num4 <= num1 and num4 <= num2 and num4 <= num3 and num4 <= num5):
        return num4
    else:
        return num5


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
num4 = int(input("Enter the fourth number: "))
num5 = int(input("Enter the fifth number: "))

print("Minimum is:", min_num(num1,num2,num3,num4,num5))
print("Maximum is:", max_num(num1, num2, num3, num4, num5))


