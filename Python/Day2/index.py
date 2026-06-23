a=int(input("Please add age: "))
if a<18:
    print("You are young and can not vote")
elif 18 <= a <= 100:
    print("You can vote")
else:
    print("Enter valid age")