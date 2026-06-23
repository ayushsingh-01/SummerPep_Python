age=int(input("Please add age: "))
if age<18:
    print("You are young and can not vote")
elif 18 <= age <= 100:
    print("You can vote")
else:
    print("Enter valid age")


salary = int(input("Please add salary: "))
if salary>1000000:
    print("Salary eligible for tier 1 gift")
elif 700000<salary<=1000000:
    print("Salary eligible for tier 2 gift")
elif 300000<salary<=500000:
    print("Salary eligible for tier 3 gift")
else:
    print("No gift")