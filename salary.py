years = int(input("Enter years of service: "))
qualification = input("Enter qualification (Masters/Bachelors): ")
# and is used when both conditions must be true
if years >= 10 and qualification == "masters":
    salary = 150000
#elif has conditions
elif years >= 10 and qualification == "bachelors":
    salary = 100000
elif years < 10 and qualification == "masters":
    salary = 100000
elif years < 10 and qualification == "bachelors":
    salary = 70000
else:
    salary = 0
    print("Invalid qualification")
if salary > 0:
    print("Your salary is:", salary)