# #print 1-10
# for i in range(1,11):
#     print(i)
#
# #even number
# for i in range(2,11,2):
#     print(i)
#
# #odd number
# for i in range(1,11,2):
#     print(i)
#
#
# #reverse number
# for i in range(10,0,-1):
#     print(i)
#
#
# #multiplication
# for i in range(1,11):
#     print("2 X ",i," = ",i*2)
#
#
#
# #sum of first n numbers
# sum=0
# for i in range(1,11):
#     sum+=i
# print(sum)


#factorial
fact=1
for i in range(1,11):
    fact*=i
print(fact)


#count digit
number=9876
s=str(number)
c=0
for i in s:
    c+=1
print(c)


#sum of digits
n=1234
suu=0

for i in str(n):
    suu+=int(i)
print(suu)

