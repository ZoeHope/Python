
name = input("Enter your name: ")
age = int(input("Enter your age: "))
if age < 100:
    ageDif = 100 - age
    answer = 2020 + ageDif
    print(name, "You will be 100 in", answer,".")

elif age == 100:
	print(name, "You are 100 years old.")

else:
    print(name, "You are already above 100.")
