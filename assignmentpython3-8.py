# NAME:- Pranav Verma
# RTU ROLL NO:- 19EARCS085
# PYTHON ASSIGNMENT
# day 3
"""
a = 105
print(type(a))
b = 105.5
print(type(b))
c = 192.6j
print(type(c))
d = 10+6j
print(type(d))
e = '10'
print(type(e))
f = 'hello world'
print(type(f))
g = [10,30,60]
print(type(f))
h = {'name': 'gunjan','age':21 ,'language': 'python'}
print(type(h))"""
# DAY 4
"""
question: 2
list1 = [1,"hi","gunjan",2]
print(type(list1))
print(list1)
print(list1[3:])
print(list1[1:2])
print(list1+list1)
print(list1*3)
list1.append(5)
list1.pop(2)
list1.remove("hi")"""
# question 3
"""
list = ["python", "rubey", "c++", "c" , "java" ]
print(type(list))
print(list)
list.remove("c++")
print(list)
list.append("computer")
print(list)
list.extend("c#")
print(list)"""
# question 4
# mutable and immutable data types in python
"""
Mutable is a fancy way of saying that the internal state of the object is changed/mutated.
So, the simplest definition is: An object whose internal state can be changed is mutable.
On the other hand, immutable doesn't allow any change in the object once it has been created.
->Some of the mutable data types in Python are list, dictionary, set and user-defined classes.
->On the other hand, some of the immutable data types are int, float, decimal, bool, string, tuple, and range.
"""
# question 5
"""
num1
FLAG
get_user_name
userDetails
_1234"""

# DAY 5
# shallow and deep copy
"""
Shallow Copy	Deep Copy
Shallow Copy stores the references of objects to the original memory address.  
Deep copy stores copies of the object’s value.
Shallow Copy reflects changes made to the new/copied object in the original object.
Deep copy doesnot reflect changes made to the new/copied object in the original object.
Shallow Copy stores the copy of the original object and points the references to the objects.
Deep copy stores the copy of the original object and recursively copies the objects as well.
Shallow copy is faster.
Deep copy is comparatively slower."""
# question 6
"""
Atomic data type:
Numeric.
Sequence Type.
Boolean.
Set.
Dictionary.
secondary data type:
Data structures that aren't supported by python but can be programmed to reflect the same functionality' 
                         ' using concepts supported by python are user-defined data structures."""
# question 7
# UDF:- user define function in python


# DAY 6
# question 1
"""
1.dital clock
2.dictionary
3.rock ,paper,scissor game
4.text to speech with python
5.send email with python
"""
# question 2
"""people = [
 {'name': "Tom", 'age': 10},
 {'name': "Mark", 'age': 5},
 {'name': "Pam", 'age': 7},
 {'name': "gunjan", 'age':20},
    {'name': "pranav", 'age':20}

]
print(people)"""
# question 3
# duck typing
"If it walks like duck, swims like duck, looks like a duck, then it probably should be a duck."

"""The above statement gives an idea to identify a duck.
Here we don't need to have a genomic sequence of the duck. We draw our conclusion by its behavior and external appearances.

We will discuss what is exactly mean of duck typing in Python programming."""
#  dunder and special method in python
"""
Dunder or magic methods in Python are the methods having two prefix and suffix underscores in the method name.
 Dunder here means “Double Under (Underscores)”. These are commonly used for operator overloading.
 Few examples for magic methods are: __init__, __add__, __len__, __repr__ etc.
"""
# question 4
# operators and its types in python
""" Operators are the constructs which can manipulate the value of operands.
 its types 
Arithmetic Operators
Comparison (Relational) Operators
Assignment Operators
Logical Operators
Bitwise Operators
Membership Operators
Identity Operators"""

# DAY 8
# QUESTION 1
"""
1. true 
2. false"""
"""a = True
print(type(a))

b = False
print(type(b))"""
# question 2
"""
1. NAD 
2. OR 
3.NOT
"""
# question 3
"""
1.AND
A  B  Y=AB
0  0    0
0  1    0
1  0    0
1  1    1

2. OR
A  B  Y=A+B
0  0    0
0  1    1 
1  0    1
1  1    1

3.NOT

A  B
0  1
1  0"""
# question 4


# question 5
""""
1.less  than( <)
2.Greater than( >)

3.less than or equal
to( <=), 
4.Greater
than or equal
to( >=) 
5.Equal
to( ==) 
6.Not
equal
to( !=)."""
# question 6

# equal to operater and assignment operater
"""
The main difference between "==" and "===" operator is that formerly compares variable by making type correction e.g.
if you compare a number with a string with numeric literal, == allows that, but === doesnot
allow that, because it not only checks the value but also type of two variable
"""
# question 7
"""
is 
True if the operands are identical (refer to the same object)	
"""

# DAY 9
# question 1
"""
a = int(input("Enter a number: "))
if a < 0:
    print("The number is negative")
elif a > 0:
    print("The number is positive")
else:
    print("The number is zero")"""


# question 2
"""
x = int(input("Enter a number: "))
if x % 5 == 0 and x % 11 == 0:
    print("The number is divisible by 5 and 11")
else:
    print("The number is not divisible by 5 and 11")
    """
# question 3
"""
year = int(input("Enter a year: "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("The year is leap year")
else:
    print("The year is not leap year")"""

#question 4
"""
char = input("Enter a character: ")
if char.isalpha():
    print("The character is alphabet")  
else:
    print("The character is not alphabet")
"""

# question 5
"""
char = input("Enter a character: ")
if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
    print("The character is vowel")
else:
    print("The character is consonant")"""

# question 6
"""
char = input("Enter a character: ")
if char.isalpha():
    print("The character is alphabet")
elif char.isdigit():
    print("The character is digit")
else:
    print("The character is special character")
"""

# question 7
"""
char = input("Enter a character: ")
if char.isupper():
    print("The character is uppercase alphabet")
elif char.islower():
    print("The character is lowercase alphabet")
else:
    print("The character is not alphabet")
    """

# question 8
"""
week = int(input("Enter a week number: "))
if week == 1:
    print("Monday")
elif week == 2:
    print("Tuesday")    
elif week == 3:
    print("Wednesday")
elif week == 4:
    print("Thursday")
elif week == 5:
    print("Friday")
elif week == 6:
    print("Saturday")
elif week == 7:
    print("Sunday")
else:
    print("Invalid week number")"""

# question 9
"""
angle1 = int(input("Enter angle 1: "))
angle2 = int(input("Enter angle 2: "))
angle3 = int(input("Enter angle 3: "))
if angle1 + angle2 + angle3 == 180:
    print("Triangle is valid")
else:
    print("Triangle is invalid")
 """

# question 10
"""
side1 = float(input("Enter side 1: "))
side2 = float(input("Enter side 2: "))
side3 = float(input("Enter side 3: "))
if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    print("Triangle is valid")
else:
    print("Triangle is invalid")"""

# question 11
"""
side1 = float(input("Enter side 1: "))
side2 = float(input("Enter side 2: "))
side3 = float(input("Enter side 3: "))
if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    if side1 == side2 == side3:
        print("Equilateral triangle")
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")
else:
    print("Invalid triangle")"""

# question 12
"""
marks = []
for i in range(5):
    marks.append(int(input("Enter marks: ")))
total = sum(marks)
percentage = total/5
if percentage >= 90:
    print("Grade A")
elif percentage >= 80:
    print("Grade B")
elif percentage >= 70:
    print("Grade C")
elif percentage >= 60:
    print("Grade D")
elif percentage >= 40:
    print("Grade E")
elif percentage < 40:
    print("Grade F")
elif percentage < 0:
    print("Invalid")"""

# question 13
"""
salary = int(input("Enter salary: "))
if salary <= 10000:
    hra = 20
    da = 80
elif salary <= 20000:
    hra = 25
    da = 90
else:
    hra = 30
    da = 95
gross_salary = salary + (salary * hra/100) + (salary * da/100)
print("Gross salary: ", gross_salary)"""

# question 14
input_unit = int(input("Enter the number of units: "))
first_50 = 50
next_50_150 = 75
next_150_250 = 120
next_250 = 250
additional_surcharge = 0.2
next_100_unit = next_50_150 + next_150_250
next_250_unit = next_250 + next_250

total_bill = 0
if input_unit <= first_50:
    total_bill = input_unit * 0.5
elif input_unit > first_50 and input_unit <= next_100_unit:
    total_bill = first_50 * 0.5 + (input_unit - first_50) * 0.75
elif input_unit > next_100_unit and input_unit <= next_250_unit:
    total_bill = first_50 * 0.5 + next_50_150 * 0.75 + (input_unit - next_100_unit) * 1.2
else:
    total_bill = (50*0.5) + (100*0.75) + (100*1.20) + (input_unit - 250) * 1.50
additional_surcharge = total_bill * additional_surcharge
total_bill = total_bill + additional_surcharge

print("Total bill is: ", total_bill)



