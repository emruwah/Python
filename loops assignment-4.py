# Q1. Write the output of the following:

#1.  for i in "Myblog":
#     print(i,'?')

# M?
# y?
# b?
# l?
# o?
# g?

# 2. for i in range(5):
#     print(i)

# 0
# 1
# 2
# 3
# 4

# 3. for i in range(10,15):
#     print(i)

# 10
# 11
# 12
# 13
# 14

# Q2. Write a program to print first 10 natural number.

# for i in range(1,11):
#     print(i)

# Q3. Write a program to print first 10 even numbers.

# for i in range(2,12,2):
#     print(i)

# Q4. Write a program to print first 10 odd numbers.

# for i in range(1,11,2):
#     print(i)

# Q5. Write a program to print first 10 even numbers in reverse order.

# for i in range(10,0,-2):
#     print(i)

# Q6. Write a program to print table of a number accepted from user.

# num=int(input("Enter any number :"))
# for i in range(1,11):
#     print(num*i)

# Q7. Write a program to display product of the digits of a number accepted from the user.

# num=int(input("Enter any number :"))
# p=1
# while(num):
#     r=num%10
#     p=p*r
#     num=num//10
# print("Product of digits is",p)

# Q8. Write a program to find the factorial of a number.

# num=int(input("Enter any number :"))
# f=1
# for i in range(1,num+1):
#     f=f*i
# print("Factorial is",f) 

# Q9. Write a program to find the sum of the digits of a number accepted from user.
# n=int(input("Enter any number :"))
# s=0
# while(n):
#     r=n%10
#     s=s+r
#     n=n//10
# print("Sum of digits is",s)

# Q10. Write a program to check whether a number is prime or not.

# n=int(input("Enter any number :"))
# f=0
# if n==1 or n==0:
#     f=1
# for i in range(2,n):
#     if n%i==0:
#         f=1
# if f==1:
#     print("Number is not prime")
# else:
#     print("Number is prime")

# Test 2

# # Q1. Write the output of the following

# 1. for i in(1,10):
#     print(i)

# 1
# 10

# 2. for i in(5,9):
#     print(i)

# 5
# 9

# 3. for i in range(2,7):
#     print(i)
    
# 2
# 3
# 4
# 5
# 6

# 4. for i in "csiplearninghub":
#     print(i)

# c
# s
# i
# p
# l
# e
# a
# r
# n
# i
# n
# g
# h
# u
# b

# 5. for i in"python":
#     print(i,end='')

# p y t h o n

# 6. for i in "python":
#     print(i,end=='?')

# p?y?t?h?o?n?

# 7. for i in "python":
    # print(i,'?$')

# p?$y?$t?$h?$o?$n?$

# 8. for i in(1,2,3,4):
#     print(i)

# 1
# 2
# 3
# 4

# 9. for i in(3,4,7):
#     print(i)

# 3
# 4
# 7

# 10. for i in range(2,10,2):
#     print(i)

# 2
# 4
# 6
# 8

# Test 3

# Q1. Write the output of the following code

# 1. x=5
    #  while(x<15):
    #  print(x**2)
    #  x+=3

# 25
# 64
# 121
# 196

# 2. a=7
    #b=5
   # while(a<9):
   # print(a+b)
   # a+=1

# 12
# 13

# 3. b=5
#    while(b<9):
#        print("H")
#        b+=1
# H
# H
# H
# H

# 4.  b=15
# while(b>9):
#     print("Hello")
#     b=b-2

# Hello
# Hello
# Hello

# 5. x=15
# while(x==15):
#     print("Hello")
#     x=x-3

# Hello

# 6. x="123"
# for i in x:
#     print("a")

# a
# a
# a

# 7. i=9
# while True:
#     if i%3==0:
#         break
#     print("A")

# Loop will not execute

# 8. a=6
# while(a<=10):
#     print("a")
#     a+=1

# a
# a
# a
# a
# a

# 9. i=0
# while i<3:
#     print(i)
#     i=i+1
# else:
#     print(7)

# 0
# 1
# 2
# 7

# 10. i=0
# while i<3:
#     print(i)
#     i=i+1
#     print(0)

# 0
# 0
# 1
# 0
# 2
# 0

# 11. i=2
# for x in range(i):
#     i+=1
#     print(i)
#     print(i)

# 3
# 3
# 4
# 4

# 12. i=2
# for x in range(i):
#     x+=1
#     print(x)
#     print(x)

# 1
# 2
# 2

# 13. i=2
# for x in range(i):
#     x+=1
#     print(x)
#     print("x")

# 1
# x
# 2
# x

# 14. i=100
# while i<57:
#     print(i)
#     1+=5

# Loop will run infinite times

# Test 4

# Q1. Write a program to print the following pattern.
# a) 
#    1
#    1 2
#    1 2 3
#    1 2 3 4

# for i in range(1,5):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# b) 
#      * * * *
#      * * *
#      * *
#      *

# for i in range(4,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# Q2. Accept 10 numbers from the user and display their average.

# s=0
# for i in range(10):
#     n=int(input("Enter number :"))
# s=s+n
# print("Average of 10 numbers is",s/10)

# Q3. Write a program to print all prime numbers that fall between two numbers including both(accept two numbers from the user)

# def primn(num):
#     f=0
#     if num==1 or num==0:
#         f=1
#     for i in range(2,num):
#         if num%i==0:
#          f=1
#     if f==1:
#         return 'n'
#     else:
#         return 'y'
# n1=int(input("Enter first number :"))
# n2=int(input("Enter second number :"))
# if n1>n2:
#     for i in range(n2,n1+1):
#         r=primn(i)
#         if r=='y':
#             print(i)
# else:
#     for i in range(n1,n2+1):
#      r=primn(i)
#     if r=='y':
#         print(i)

# Q4. Write a program to display sum of odd numbers and even numbers that fall between 12 and 37(including both numbers)

# so=0
# se=0
# for i in range(12,38):
#     if i % 2==0:
#         se=se+i
#     else:
#         so=so+i
# print("Sum of all even numbers is",se)
# print("Sum of all odd numbers is",so)

# Q5. Write a program to display all the numbers which are divisible by 11 but not by 2 between 100 and 500.

# for i in range(100,500):
#     if i%11==0 and i%2!=0:
#         print(i)

# Q6. How many times the following loop execute?
# c=0
# while c<20:
#     c+=2

# The loop will run ten times

# Write the output of the following:
# c=-9
# while c<20:
#     c+=3
#     print(c)

# -6
# -3
# 0
# 3
# 6
# 9
# 12
# 15
# 18
# 21

# Q8. Write a program to print numbers from 1 to 20 except multiple of 2 & 3.

# for i in range(1,21):
#     if i%2!=0 and i%3!=0:
#         print(i)

# Q9. Write a program to print table of a number (accepted from user) in the following format.
    # Like:input number is7, so expected output is
# 7*1=7
# 7*2=14 and so on

# n=int(input("Enter any number :"))
# for i in range(1,11):
#     print(n,"*",i,"=",n*i)

# Q10. Write a program that keep on accepting number from the user until user enters zero. Display the sum and average of all the numbers.

# n=1
# i=-1
# s=0
# while(n!=0):
#     n=int(input("Enter any number :"))
#     s=s+n
#     i=i+1
# print("Average of numbers entered by you is",s/i)

# Test 5

# Q1. Write a program to print the following pattern.
# 5 5 5 5 5
# 4 4 4 4 
# 3 3 3
# 2 2
# 1

# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()

# Q2. Find errors in the following code:

# a=int("Enter any number :")
# for i in range[2,6]:
#     if a==i:
#         print("A")
# else:
#     print("B")

# Q3. Write a program to accept decimal number and display its binary number.

# n=int(input("Enter any number :"))
# l=[]
# while(n):
#     r=n%2
#     l.append(r)
#     n=n//2
# for i in range(len(l)-1,-1,-1):
#     print(l[i],end=" ")

# Q4. Accept a number and check whether it is pallindrome or not.

# n=int(input("Enter any number :"))
# ornum=n
# rn=0
# while(n):
#     r=n%10
#     rn=rn*10+r
#     n=n//10
# if ornum==rn:
#     print("Number is Pallindrome")
# else:
#     print("Number is not a Pallindrome")

# Q5. Write a program to accept a number and check whether it is a perfect number or not.
# (Perfect number is  a positive integer which is equal to the sum of its divisors like divisors of 6 are 1,2,3 and
#  sum of divisors is also 6,so 6 is the perfect number)

# n=int(input("Enter any number :"))
# s=0
# for i in range(1,n):
#     if n%i==0:
#      s=s+i
# if n==s:
#     print("Number is perfect")
# else:
#      print("Number is not perfect")

# Q6. Write a program to find the sum of the following series(accept values of x and n from user) 
# 1+x/1!+x2/x2!+.......xn/n!

# import math
# n=int(input("Enter number of terms :"))
# x=int(input("Enter the base :"))
# s=1.0
# for i in range(1,n+1):
#     s=s+math.pow(x,i)/math.factorial(i)
#     print(s)

# Q7. Write a program to print the following pattern
# A
# B C 
# D E F 
# G H I J 
# K L M N O 

# l=65
# for i in range(1,6):
#     for j in range(1,i+1):
#      print(chr(l),end=" ")
#     l=l+1
# print()
# l=65 

# Q8. Write the output of the following:
# for x in range(10,20):
#     if(x%2==0):
#         continue
#     print(x)

# Q9. Write a function to display prime numbers below any number accepted from the user.

# def primn(num):
#     f=0
#     if num==1 or num==0:
#         f=1
#     for i in range(2,num):
#         if num%i==0:
#             f=1
#         if f==1:
#             return 'n'
#         else:
#             return 'y'
# num=int(input("Enter number :"))
# for i in range(num):
#     r=primn(i)
#     if r=='y':
#         print(i)

# Test 6

# Q1. Write the output of the following:
# a=5
# while a>0:
#     print(a)
#     a=a-1

# Q2. for loop statement is terminated by symbol ________
#     Semicolon(;)

# Q3. What is the difference between break and continue statements?

# break statement terminates the loop as the condition matches.for example
# a=5
# while a>0:
#     a=a-1
#     if a==3:#as this condition matches it terminates the loop
#         break
#     else:
#         print(a)
# Output: 4

# Continue statement is used to skip a particular condition.for example
# a=5
# while a>0:
#     a=a-1
#     if a==3# as this condition matches it goes to the next condition of the loop
#     continue
# else:
# #     print(a)
# Output :
# 4
# 2
# 1
# 0

# Q4. Convert the following loop into for loop:
# x=4
# while(x<=8):
#     print(x*10)
#     x+=2

# for x in range(4,9,2):
#     print(x*10)

# Q5. Write the output of the following:
# for k in range(10,20,4):
# print(k)

# 10
# 14
# 18

# Q6. Find errors in the following code:
# x=input("Enter value")
# for k in range[0,20]
# if x=k
# print(x+k)
# else:
# Print(x-k)

# x=input("Enter value")
# for k in range(0,20):
#     if x==k:
#         print(x+k)
#     else:
#         print(x-k)

# Q7. Write the output of the following:
# x=3
# if x>2 or x<5 and x==6:
#     print("Bye")
# else:
#     print("Thank you")

# Bye

# Q8. Write the output of the following:
# x,y=2,4
# if(x+y==10):
#     print("Thankyou")
# else:
#     print("Bye")

# Bye

# Q9. Write the output of the following:
# x=10
# y=1
# while x>y:
#     x=x-4
#     y=y+3
#     print(x)

# 6
# 2

# Q10. Write the output of the following:
# for x in range(3):
#     for y in range(2):
#         print("Practice Questions of loops in python")
#         print()

# Practice Questions of loops in python
# Practice Questions of loops in python


# Practice Questions of loops in python
# Practice Questions of loops in python

# Practice Questions of loops in python
# Practice Questions of loops in python



