#This function reverses a string.

def reverse(text):
    a = ""
    for i in range(1, len(text) + 1):
        a += text[len(text) - i]
    return a

print("This is before reversing, the sting is 'Hello World!'.")
print("After: ")
print(reverse("Hello World!"))
