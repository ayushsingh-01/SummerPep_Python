# age=int(input("Please add age: "))
# if age<18:
#     print("You are young and can not vote")
# elif 18 <= age <= 100:
#     print("You can vote")
# else:
#     print("Enter valid age")
#
#
# salary = int(input("Please add salary: "))
# if salary>1000000:
#     print("Salary eligible for tier 1 gift")
# elif 700000<salary<=1000000:
#     print("Salary eligible for tier 2 gift")
# elif 300000<salary<=500000:
#     print("Salary eligible for tier 3 gift")
# else:
#     print("No gift")

#using function
# def isprime(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#
#     return True
# number=int(input("Enter number to check"))
# print(isprime(number))




#zomato coupon
# from datetime import datetime
# name=str(input("Enter your name"))
# birthday=str(input("Enter birthday in format yyyy-mm-dd"))
# date_object = datetime.strptime(birthday, "%Y-%m-%d")
# birthday_month=date_object.month
# number_of_order=10
# total_spent=1110
# if date_object.month==date_object.month and total_spent>1000 and number_of_order>5:
#     print("highest order discount with birthday discount")
# elif birthday_month==date_object.month:
#     print("Birthday month discount!!!!")
# elif number_of_order>5:
#     print("returning customer discount")
# elif total_spent>1000:
#     print("high value customer discount")



user_name = input("Enter your username: ")
password = input("Enter your password: ")
saved_password = "122345"
saved_username = "yesss"

if user_name == saved_username and password == saved_password:
    print("Welcome " + user_name)
else:
    print("Wrong name/password")


