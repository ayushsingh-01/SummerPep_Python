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


# #factorial
# fact=1
# for i in range(1,11):
#     fact*=i
# print(fact)
#
#
# #count digit
# number=9876
# s=str(number)
# c=0
# for i in s:
#     c+=1
# print(c)
#
#
# #sum of digits
# n=1234
# suu=0
# for i in str(n):
#     suu+=int(i)
# print(suu)




#palindrome number
a=int(input())
c=a
b=0
while a>0:
    r=a%10
    b=(b*10)+r
    a=a//10
if c==b:
    print("YES")
else:
    print("NO")




#reverse number
num=1234
r_num=0
while num!=0:
    d=num%10
    r_num=(r_num*10)+d
    num//=10
print(r_num)


#fibonacci
len=10
a,b=0,1
c=0
while c<len:
    print(a," ")
    a,b=b,a+b
    c+=1

#prime number
num=int(input())
if num<=1:
 print("not prime")
else:
 divisor=2
 is_prime=True
 while divisor*divisor<=num:
  if num%divisor==0:
   is_prime=False
   break
  divisor+=1
if is_prime:
  print("is prime")
else:
  print("not prime")
