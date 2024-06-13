# ASSIGNMENT 1
# 1. Write a Python program to swap the values of two variables without using a temporary variable.

# ANS. a=3
# b=7
# a,b=b,a

# print(a)
# print(b)

# 2. Calculate the area of a circle given its radius. Take the radius as input from the user.

#ANS.  r=float(input("Enter the radius of a circle :"))
# a= 3.14*r*r
# print(a)

# 3. Write a Python program to check if a number is even or odd.

#ANS.  number=int(input("Enter a number :"))
# if (number%2)==0:
#     print("The number is even")
# else:
#     print("The number is odd")

# 4. Calculate the factorial of a number using a loop.

#ANS.  n=int(input("Enter the number : "))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)

# 5. Convert a given temperature in Fahrenheit to Celsius using the formula. C= (F-32)*5/9

# ANS. F=int(input("Enter the Fahrenheit :"))
# C=(F-32)*5/9
# print("The temperature in celsius :" , C)


# LISTS AND SLICING:

# 1. Create a list of 10 numbers. Write a Python program to print the even numbers from the list.

#ANS.  l1=[1,2,3,4,5,6,7,8,9,10]
# for number in l1:
#    if (number%2==0):
#      print(number)

# 2. Given a list of strings, write a program to count how many strings have a length of 5 or more characters.

# s1=["apple","mango","orange","grape","pineapple"]



# 3. Slice a given list to print only the first and the last three elements.

# ANS. l1="apple,mango,orange,grape,pineapple"
# print(l1[:5])
# print(l1[-22:])

# 4. Reverse a list without using the reverse() method.

# ANS. num=[1,2,3,4,5]
# wes=[]
# for i in range(len(num)-1,-1,-1):
#     print(i)

# 5. Find the maximum and minimum values in a list.

# value=eval(input("Enter a list :"))
# print("The list is :", value)
# max=max(value)
# min=min(value)
# print("The maximum number is :" ,max)
# print("The minimum number is :", min)


# CONDITIONAL STATEMENTS: IF,IF-ELSE,ELIF STATEMENTS

# 1. Write a Python program to check if a given number is positive,negative,or zero.

# num=int(input("Enter the number :"))

# if(num>0):
#     print("The number is a positive number" ,num)
# elif(num<0):
#     print("The number is negative number" ,num)
# else:
#     print("Number is zero")

# 2. Check if a student's grade is an 'A','B','C','D',or 'F' based on their test score.

# marks=int(input("Enter the score :"))
# grade=""

# if(marks>=80):
#     grade="A Grade"
# elif(marks>=60):
#     grde="B Grade"
# elif(marks>=40):
#     grade="C Grade"
# elif(marks>=35):
#     grade="D Grade"
# else:
#     grade="F Grade"
# print("Marks :", marks)
# print("Grade :", grade)

# 3. Determine if a year is a leap year or not.

# Year=int(input("Enter the year :"))
# if(Year % 400 ==0):
#     print(Year, "The year is a leap year")
# elif(Year % 4 ==0 and Year % 100!=0):
#     print(Year, "The year is a leap year")
# else:
#     print(Year, "The year is not a leap year")


# 4. Check if a number is prime or not.

# num=int(input("Enter a number :"))
# for i in range(2,num):
#     if num % i==0:
#         print("not a prime")
#         break 
#     else:
#         print("prime")

# 5. Determine if a user-provided character is a vowel or a consonant.

# char=input("Enter the alphabet :")
# if char in('a','e','i','o','u','A','E','I','O','U'):
#     print(char, "is a vowel")
# else:
#     print(char, " is a consonant")

# ITERATIVE STATEMENTS : FOR LOOP

# 1. Write a Python program to print the numbers from 1 to 10 using a for loop.

# for x in range(11):
#     print(x)

# 2. Calculate the sum of all even numbers from 1 to 50 using a for loop.

# for i in range(51):
#     if i%2==0:
#         print(i)
        

# 3. Generate a Fibonacci sequence of n terms using a for loop.

# def fib(n):
#     a = 0
#     b = 1
#     if n == 1:
#         print(a)
#     else:
#         print(a)
#         print(b)

#         for i in range(2,n):
#             c = a+b
#             a = b
#             print(c)

# fib(2)

# 4. Calculate the factorial of a number using a for loop and a function.



# 5. Write a program to find and print all the prime numbers between 1 to 100.
# 


# ITERATIVE STATEMENTS : WHILE LOOP 

# 1. Write a Python program to print the numbers from 1 to 10 using a while loop.

# num=1
# while num<=10:
#     print(num)
#     num=num+1
# 2. Calculate the sum of all odd numbers from 1 to 50 using a while loop.

# n=50
# sum=0
# i=1
# while i<=n:
#     if(i%2==1):
#         print(i)
#         sum=sum+1
#     i=i+1
# print("sum=",sum)

# 3. Use a while loop to reverse a given string.


# 4. Implement a simple guessing game where the user has to guess a number between 1 and 100.

# import random
# num=random.randint(1,100)
# guess=0

# while guess!= num:
#     guess=int(input("Enter Guess:"))

#     if(guess < num):
#         print("Guess Higher! :")
#     elif(guess > num):
#         print("Guess lower! :")
#     else:
#         print("You won")

# 5. Write a program to find and print all the even numbers between 1 and 100 using a while loop.

# i=1
# while i<=100:
#     if i%2==0:
#         print(i)
#     i=i+1


# ITERATIVE STATEMENTS : NESTED FOR LOOP

# 1. Write a Python program to print a multiplication table (1 to 10) using nested for loops.

# n=int(input("Enter the number :"))
# for i in range(1,11):
#     print(n,"*",i,"=",n*i)

# 2. Create a square pattern of a specified size using asterisks.
# * * * *
# * * * *
# * * * *
# * * * *

# num=int(input("Enter the rows :"))
# for i in range(num):
#     print("* "*num)

# 3. Create a pattern of a asterisks in the form of a right-angled triangle.
#  * 
# * *
# * * *
# * * * *
# * * * * *

# num=int(input("Enter the number of rows :"))
# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print("*" ,end=" ")
#     print()

# 4. Generate a pattern of numbers in the form of a right-angled triangle.
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# n=int(input("Enter the number of rows :"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j ,end=" ")
#     print()
        
# 5. Create a pattern of a alphabets in the form of an equilateral triangle.
# P 
# P Y 
# P Y T 
# P Y T H 
# P Y T H O 
# P Y T H O N 

# str=input("Enter the str :")
# length=len(str)
# for i in range(length):
#     for j in range(i+1):
#         print(str[j],end=" ")
#     print()


