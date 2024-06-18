# Test 1
# 1. Name the keyword which helps in writing code involves condition.
# ans. if

# 2. Write the synatx of simple if statement.
# ans. if <Condition>:
    
# 3. Is there any limit of statement that can appear under an if block.
# ans. No

# 4. Write a program to check whether a person is eligible for voting or not.(accept age from user)
# age=int(input("Enter your age :"))
# if age>=18:
#     print("Eligible for voting")
# else:
#     print("not eligible for voting")

# 5.Write a program to check whether a number entered by user is even or odd.
# num=int(input("Enter a number :"))
# if num % 2==0:
#     print("Number is even")
# else:
#     print("Number is odd")

# 6. Write a program to check whether a number is divisible by 7 or not.
# num=int(input("Enter a number :"))
# if num % 7==0:
#     print("Number is divisible")
# else:
#     print("Number is not divisible")

# 7. Write a program to display "Hello" if a number entered by user is a multiple of five, otherwise print "Bye"

# num=int(input("Enter a number :"))
# if num%5==0:
#     print("Hello")
# else:
#     print("Bye")

# 8. Write a program to calculate the electricity bill(accept number of unit from user) according to the following criteria:
# Unit
# price
# First 100 units
# no charge
# Next 100 units
# Rs 5 per unit
# After 200 units
# Rs 10 per unit
# (For example if input unit is 350 than total bill amount is Rs2000)
# amt=0
# num=int(input("Enter number of electric unit :"))
# if num<=100:
#     amt=0
# if num>100 and num<=200:
#     amt=(num-100)*5
# if num>200:
#     amt=500+(num-200)*10
# print("Amount to pay" ,amt)

# 9.Write a program to display the last digit of a number.(hint : any number % 10 will return the last digit)
# num=int(input("Enter any number :"))
# print("Last digit of number is", num%10)

# 10.Write a program to check whether the last digit of a number (entered by user) is divisible by 3 or not.
# num=int(input("Enter any number :"))
# id=num%10
# if id%3==0:
#     print("Last digit of number is divisible by 3")
# else:
#     print("Last digit of number is not divisible by 3")

# Test 2

# 1. Write a program to accept percentage from the user and display the grade according to the following criteria.
# Marks            Grade
# >90                A
# >80 and <=90       B
# >=60 and <=80      C
# below 60           D

# per=int(input("Enter marks :"))
# if per>90:
#     print("Grade is A")
# if per>80 and per<=90:
#     print("Grade is B")
# if per>=60 and per<=80:
#     print("Grade is C")
# if per<60:
#     print("Grade is D")

# 2. Write a program to accept the cost price of a bike and display the road tax to be paid according to the following criteria :
# Cost price (in Rs)
# Tax 
#    >100000
# 15%
#    >50000 and <=100000
# 10%
#    <=50000
# 5%

# tax=0
# pr=int(input("Enter the price of a bike:"))
# if pr >100000:
#     tax=15/100*pr
# elif pr>50000 and pr<=100000:
#     tax=10/100*pr
# else:
#     tax=5/100*pr
# print("Tax to be paid", tax)

# 3. Write a program to check whether an year is leap year or not.

# yr=int(input("Enter the year :"))
# if yr%100==0:
#     if yr%400==0:
#         print("Entered year is leap year")
#     else:
#         print("Entered year is not a leap year")
# else:
#     if yr%4==0:
#         print("Entered year is leap year")
#     else:
#         print("Entered year is not a leap year")

# 4. Write a program to accept a number from 1 to 7 and display the name of the day like 1 for Sunday, 2 for Monday and so on.

# num=int(input("Enter any number between 1 to 7 :"))
# if num==1:
#     print("Sunday")
# elif num==2:
#     print("Monday")
# elif num==3:
#     print("Tuesday")
# elif num==4:
#     print("Wednesday")
# elif num==5:
#     print("Thursday")
# elif num==6:
#     print("Friday")
# elif num==7:
#     print("Saturday")
# else:
#     print("Please enter number between 1 to 7")

# 5. Write a program to accept a number from 1 to 12 and display name of the month and days in that month like 1 for January and number of days 31 and so on. 

# num=int(input("Enter any number between 1 to 12 :"))
# if num==1:
#     print("January")
# elif num==2:
#     print("February")
# elif num==3:
#     print("March")
# elif num==4:
#     print("April")
# elif num==5:
#     print("May")
# elif num==6:
#     print("June")
# elif num==7:
#     print("July")
# elif num==8:
#     print("August")
# elif num==9:
#     print("September")
# elif num==10:
#     print("October")
# elif num==11:
#     print("November")
# elif num==12:
#     print("December")
# else:
#     print("Please enter number 1 to 12")

# 6. What do you mean by statement?

# Executable lines in a program is called instruction.

# 7. Write the output of the following:
# if True:
#     print(101)
# else:
#     print(202)


# 8. Write the logical expression for the following:
    # A is greater than B and C is greater than D.

# A>B and C<D

# Accept any city from the user and display monument of that city.
# City                 Monument
# Delhi                Red Fort
# Agra                 Taj Mahal
# Jaipur               Jal Mahal

# city=input("Enter the name of the city :")
# if city.lower()=="delhi":
#     print("Monument name is : Red Fort")
# elif city.lower()=="agra":
#     print("Monument name is : Taj Mahal")
# elif city.lower()=="jaipur":
#     print("Monument name is : Jal Mahal")
# else:
#     print("Enter correct name of city")

# 10. Write the output of the following 
# if a=9:
#     if (a>5 and a <=10):
#      print("Hello")
#     else:
#         print("Bye")


# Test 3

# 1. Write a program to check whether a number entered is three digit number or not.

# num=(input("Enter any number"))
# l=len(num)
# if l !=3:
#     print("Enter three digit number")
# else:
#     print("The number is a three digit number")

# 2. Write a program to check whether a person is eligible for voting or not(voting age>=18)

# age=int(input("Enter your age :"))
# if age >18:
#     print("Eligible for voting")
# else:
#     print("Not eligible for voting")

# 3. Write a program to check whether a person is senior citizen or not.

# age=int(input("Enter your age :"))
# if age>=60:
#     print("Senior Citizen")
# else:
#     print("Not a Senior Citizen")

# 4. Write a program to find the lowest number out of two numbers excepted from user.

# num1=int(input("Enter first number :"))
# num2=int(input("Enter second number :"))
# if num1>num2:
#     print("Smaller number is :", num2)
# else:
#     print("smaller number is :", num1)

# 5. Write a program to find the largest number out of two numbers excepted from user.

# num1=int(input("Enter first number :"))
# num2=int(input("Enter second number :"))
# if num1>num2:
#     print("greater number is :", num1)
# else:
#     print("greater number is :",num2)

# 6. Write a program to check whether a number(accepted from user) is positive or negative.

# num=int(input("Enter first number :"))
# if num>0:
#     print("Positive")
# else:
#     print("Negative")

# 7. Write a program to check whether a number is even or odd.

# n=int(input("Enter a number :"))
# if n%2==0:
#     print("Even")
# else:
#     print("Odd")

# 8. Write a program to check whether a number (accepted from user) is divisible by 2 and 3 both.

# n=int(input("Enter a number :"))
# if n%2==0 and n%3==0:
#     print("Number is divisible by 2 and 3 both")
# else:
#     print("Number is not divisible by both")

# 9. Write a program to find the largest number out of three numbers expected from user.

# n1=int(input("Enter 1st number :"))
# n2=int(input("Enter 2nd number :"))
# n3=int(input("Enter 3rd number :"))
# if n1>n2 and n1>n3:
#     print("Greatest number is ", n1)
# if n2>n1 and n2>n3:
#     print("Greatest number is" ,n2)
# if n3>n2 and n3>n1:
#     print("Greatest number is" ,n3)

# Test 4

# 1. Accept the temperature in degree Celsius of water and check whether it is boiling or not (boiling point of water in 100 C)
  
# temp=int(input("Enter temperature of water"))
# if temp>=100:
#     print("Water is boiling")
# else:
#     print("Water is not boiling")

# 2.         is a graphical representation of steps(algorithm/flow chart)

# Flow chart

# 3. Python has           statement as empty statement(Pass/Fail)

# Pass

# 4. In python, a block is a group of        statement having same indentation level.(consecutive/alternate)

# Consecutive

# 5.Out of "elif" and "else if" , which is the correct statement in python?

# elif

# 6. Accept the age of 4 people and display the youngest one?

# a1=int(input("Enter age of 1st person :"))
# a2=int(input("Enter age of 2nd person :"))
# a3=int(input("Enter age of 3rd person :"))
# a4=int(input("Enter age of 4th person :"))
# if a1<a2 and a1<a3 and a1<a4:
#     print("Age of youngest person is", a1)
# if a2<a1 and a2<a3 and a2<a4:
#     print("Age of youngest person is" ,a2)
# if a3<a2 and a3<a1 and a3<a4:
#     print("Age of youngest is", a3)
# if a4<a1 and a4<a2 and a4<a3:
#     print("Age of youngest person is" ,a4)

# 7. What is the purpose of else in if elif ladder?

# If none of the condition is true in elif ladder then the else part will execute.

# 8. 8. Accept the age of 4 people and display the oldest one.

# a1=int(input("Enter age of 1st person :"))
# a2=int(input("Enter age of 2nd person :"))
# a3=int(input("Enter age of 3rd person :"))
# a4=int(input("Enter age of 4th person :"))
# if a1>a2 and a1>a3 and a1>a4:
#     print("Age of oldest person is ", a1)
# if a2>a1 and a2>a3 and a2>a4:
#     print("Age of oldest person is ", a2)
# if a3>a2 and a3>a1 and a3>a4:
#     print("Age of oldest person is", a3)
# if a4>a1 and a4>a2 and a4>a3:
#     print("Age of oldest person",a4)

# 9. Write a program to check whether a number is prime or not.

# n=0
# num=int(input("Enter any number :"))
# if num==0 or num==1:
#     n=1
# for i in range(2,num):
#     if num%i==0:
#         n=1
# if n==1:
#     print("Number is not prime")
# else:
#     print("Number is prime")

# 10. Write a program to check a character is vowel or not.

# ch=input("Enter any character :")
# v="aeiouAEIOU"
# if ch in v:
#     print("Entered character is vowel")
# else:
#     print("Entered character is not a vowel")

# Test 5

# 1. Accept the following from the user and calculate the percentage of class attended:
# a. Total number of working days
# b. Total number of days for absent.

# After calculating percentage show that, if the percentage is less than 75, then studennt will not be able to sit in exam.

# n=int(input("Enter total number of working days :"))
# a=int(input("Enter number of days absent :"))
# per=(n-a)/n*100
# print("Your attendance is", per)
# if per<75:
#     print("You are not eligible for exams")
# else:
#     print("You are eligible for writing exam")

# 2. Accept the percentage from the user and display the grade according to the following criteria:
# Below 25--D
# 25 to 45--C
# 45 to 50--B
# 50 to 60--B+
# 60 to 80--A
# Above 80--A+

# p=int(input("Enter percentage :"))
# if p>80:
#     print("Grade is A+")
# elif p>60 and p<=80:
#     print("Grade is A")
# elif p>50 and p<=60:
#     print("Grade is B+")
# elif p>45 and p<=50:
#     print("Grade is B")
# elif p>25 and p<=45:
#     print("Grade is C")
# elif p<25:
#     print("Grade is D")

# 3. A company decided to give bonus to employee according to following criteria:
# Time period of service             Bonus
# More than 10 years                  10%
# >=6 and <=10                        8%
# Less than 6 years                   5%

# Ask user for their salary and years of service and print the net bonus amount.

# s=int(input("Enter the time period of service :"))
# sal=int(input("Enter your salary :"))
# if s>10:
#     b=10/100*sal
# if s>=6 and s<=10:
#     b=8/100*sal
# if s<6:
#     b=5/100*sal
# print("Bonus is",b)

# 4. Accept the marked price from the user and calculate the Net amount as (Marked Price-Discount) to pay according to following criteria:
# Marked Price       Discount
# >10000                20%
# >7000 and <=10000     15%
# <=7000                10%

# na=0
# d=0
# mp=int(input("Enter marked price :"))
# if mp>10000:
#     d=20/100*mp
# if mp>7000 and mp<=10000:
#     d=15/100*mp
# if mp<=7000:
#     d=10/100*mp
# na=mp-d
# print("Net amount to pay", na)

# 5. Write a program to accept percentage and display the Category according to the following criteria:
# Percentage           Category
# <40                   Failed 
# >=40 & <55            Fair 
# >=55 & <65            Good
# >=65                  Excellent

# p=int(input("Enter the percentage :"))
# if p<40:
#     print("Your Category is : Failed")
# if p>=40 and p<55:
#     print("Your Category is : Fair")
# if p>=55 and p<65:
#     print("Your Category is : Good")
# if p>=65:
#     print("Your Category is : Excellent")

# 6. Accept three sides of triangle and check whether it is an equilateral, isosceles or scalene triangle.
# note:
# An equilateral triangle is a triangle in which all three sides are equal.
# A scalene triangle is a triangle that has three unequal sides.
# An isosceles triangle is a triangle with(at least) two equal sides.

# s1=int(input("Enter the 1st side of triangle :"))
# s2=int(input("Enter the 2nd side of triangle :"))
# s3=int(input("Enter the 3rd side of triangle :"))
# if s1==s2 and s2==s3:
#     print("Equilateral triangle")
# if (s1==s2 and s2!=s3) or(s2==s3 and s2!=s1) or (s1==s3 and s1!=s2):
#     print("Isosceles triangle")
# if s1!=s2 and s1!=s3 and s2!=s3:
#     print("Scalene triangle")

# 7. Write a program to accept two numbers and mathematical operators and perform operation accordingly.
# like:
# Enter First Number :7
# Enter Second Number:9
# Enter operator:+
# Your answer is:16

# n1=int(input("Enter first number :"))
# n2=int(input("Enter second number :"))
# op=input("Enter mathematical operator :")
# if op=="+":
#     print("Result is" ,n1+n2)
# if op=="-":
#     print("Result is" ,n1-n2)
# if op=="*":
#     print("Result is" , n1*n2)
# if op=="/":
#     print("Result is" ,n1/n2)
# if op=="%":
#     print("Result is" ,n1%n2)
# if op=="**":
#     print("Result is" ,n1**n2)
# if op=="//":
#     print("Result is", n1//n2)

# 8. Accept the age, sex('M','F'), number of days and display the wages accordingly.
# Age             Sex        Wage/day
# >=18 and <30     M           700
# >=18 and <30     F           750
# >=30 and <=40    M           800
# >=30 AND <=40    F           850

# If age does not fall in any range then display the following message: "Enter appropriate age"

# a=int(input("Enter your age :"))
# s=input("Enter sex(M/F) :")
# nd=int(input("Enter number of days :"))
# if a>=18 and a<30 and s.upper()=="M":
#     amt=nd*700
# elif a>=18 and a<30 and s.upper ()=="F":
#     amt=nd*750
#     print("Total wages is :",amt)
# elif a>=30 and a<=40 and s.upper ()=="M":
#     amt=nd*800
# elif a>=30 and a<=40 and s.upper()=="F":
#     amt=nd*850
#     print("Total wages is :",amt)
# else:
#     print("Enter appropriate age")

# Test 6

# 1. Accept three numbers from the user and display the second largest number.

# n1=int(input("Enter 1st number :"))
# n2=int(input("Enter 2nd number :"))
# n3=int(input("Enter third number :"))
# if (n1>n2 and n1<n3) or (n1<n2 and n1>n3):
#     print("Middle number is", n1)
# if (n2>n1 and n2<n3) or (n2<n1 and n2>n3):
#     print("Middle number is",n2)
# if (n3>n2 and n3<n1) or (n3<n2 and n3>n1):
#     print("Middle number is",n3)

# 2. Accept three sides of triangle and check whether the triangle is possible or not.

# s1=int(input("Enter 1st side of triangle :"))
# s2=int(input("Enter 2nd side of triangle :"))
# s3=int(input("Enter 3rd side of triangle :"))
# if s1+s2>s3 and s2+s3>>s1 and s1+s3>s2:
#     print("Triangle is possible")
# else:
#     print("Triangle is not possible")

# 3. Consider the following code:
# if i<j:
#     if j<k:
#         i=j
#     else:
#         j=k

# else:
#     if j>k:
#         j=i
#     else:
#         i=k
# print(i,j,k)

# What will be the above code print if the variables i.j and k have the following values?.
# a) 1=3,j=5,k=7
# b) i=-2,j=-5,k=9
# c) i=8,j=15,k=12
# d) i=13,j=15,k=13
# e) i=3,j=5,k=17
# f) i=25,j=15,k=17

# a) 5 5 7
# b) 9 -5 9
# c) 8 12 12
# d) 13 13 13
# e) 5 5 17
# f) 17 15 17

# 4. Accept the electric units from user and calculate the bill according to the following rates.
# First 100 units :Free
# Next 200 units :Rs 2 per day
# Above 300 units :Rs 5 per day
# if number of unit is 500 then total bill=0+400+1000+1400.

# ut=int(input("Enter number of units :"))
# if ut<=100:
#     amt=0
# elif ut>100 and ut<=300:
#     amt=(ut-100)*2
# else:
#     amt=400+(ut-300)*5
# print("Total amount to pay is",amt)

# 5. Accept the number of days from the user and calculate the charge for library according to following:
#     Till five days:Rs 2/day
# Six to ten days:Rs 3/day
# After 15 days:Rs 5/day

# nd=int(input("Enter number of days :"))
# if nd<=5:
#     amt=nd*2
# elif nd>=6 and nd<=10:
#     amt=nd*3
# elif nd>=11 and nd<=15:
#     amt=nd*4
# else:
#     amt=nd*5
#     print("Total amount pay is",amt)

# 6. Accept the kilometers covered and calculate the bill according to the following criteria:
# First 10Km Rs 11/km
# Next 90Km  Rs 10/km
# After that Rs.9/km

# km=int(input("Enter the kilometer covered :"))
# if km<=10:
#     amt=km*11
# elif km>10 and km<=100:
#     amt=110+(km-10)*10
# elif km>100:
#     amt=1010+(km-100)*9
#     print("Total amount to pay is",amt)

# 7. Accept the marks of English,Maths,Science,Social Studies Subject and disply the stream alloted according the following 
# All SUbjects more than 80 marks-Scince Stream
# English>80 and Math, Science above 50-Commerce stream
# English>80 and Social studies>80-Humanities

# eng=int(input("Enter the mark of English :"))
# math=int(input("Enter the mark of Maths :"))
# sci=int(input("Enter the mark of science :"))
# ss=int(input("Enter the mark of social :"))
# if eng and math and sci and ss>80:
#     print("Science Stream")
# elif (eng>80 and math) and sci>50:
#     print("Commerce Stream")
# elif eng>80 and ss>80:
#     print("Humanities")

# Test 7

# Q1. Evaluate the following statements:
# a=True
# b=True
# c=True
# d=True
# 1. print(c)
# True
# 2. print(d)
# True
# 3. print(not a)
# False
# 4. print(not b)
# False
# 5. print(not c)
# False
# 6. print(not d)
# False
# 7. print(a and b)
# True
# 8. print(a or b)
# True
# 9. print(a and c)
# True
# 10. print(a or c)
# True
# 11. print(a and d)
# True
# 12. print(a or d)
# True
# 13. print(b and c)
# True
# 14. print(b or c)
# True
# 15. print(a and b or c)
# True
# 16. print(a or b and c)
# True
# 17. print(a and b and c)
# True
# 18. print(a or b or c)
# True
# 19. print(not a and b and c)
# False
# 20. print(not a or b or c)
# True
# 21. print(not(a and b and c))
# False
# 22. print(not(a or b or c))
# False
# 23. print(not a and not b and not c)
# False
# 24. print(not a or not b or not c)
# False
# 25. print(not(not a or not b or not c))
# True