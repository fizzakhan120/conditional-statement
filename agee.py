age = int(input("Enter your age: "))
if age < 0:
    print("Invalid age")
elif age < 2:
    print("The person is a Baby")
elif age < 4:
    print("The person is a Toddler")
elif age < 13:
    print("The person is a Kid")
elif age < 20:
    print("The person is a Teenager")
elif age < 65:
    print("The person is an Adult")
else:
    print("The person is an Elder")
