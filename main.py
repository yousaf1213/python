# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
a=5
b=5
print("There were two users Whose names are:")
print("Yousaf\nAhsan")
print("POints are as follow")
print("5\t5")
print('\\\'-\'\\\-\\')
print("this is","\\\\","double BackSlash")
#newline
print("this is","'/\\/\\/\\/\\/\\'","Mountain")
print("he is\tawesome")
print('\\\"\\n\\t\\\'')

if a>b:
    print("A is greater than B","\U0001F923")
elif b>a:
    print("B is greater than A","\U0001F923")
else:
    print("Both are equal","\U0001F923")

print(2*3)
print(2+3)
print (round(2/3,4))
print(3//3)
print(2**3)
first_name="Yousaf"
last_name="zahid"
full_name=first_name+" "+last_name
print(full_name+" "+str(3))
number1=int(input("enter your first number:"))
number2=int(input("enter your Second number:"))
number3=int(input("enter your third number:"))
total=(f"average of these numbers is:\t {(number1 + number2 + number3)/3}")
print(total)

user1=input("enter your name")
print(f"Your name length is:{len(user1)}")
print(f"Your name in lower case is:{user1.lower()}")
print(f"Your name in lower case is:{user1.upper()}")
print(f"Universal order of writing your name is:{user1.title()}")
print(f"Your reverse name is:{user1[::-1]}")
get=input("enter the occurences of letter you want to find")
print(user1.count(get))

user2,check=input("enter your name and the letter you want to search").split(",")
print(f"Total count of your alphabets is:\t{len(user2.strip())}")
print(f"Number of occurances of letter in your name is:\t{user2.strip().lower().count(check.strip().lower())}")

user3= "rangar Rao"
print(user3.replace(" ","_",1))

user4=input("enter your name")
print(user4.center(len(user4)+8,"*"))
import random
rand=random.randint(0,9)
user_guess=int(input("enter your guess number"))
if user_guess>rand:
    print("You entered greater number")
elif user_guess<rand:
    print("you entered smaller number")
else:
    print("Congratulations you won")
def my_function(data):
  for x in  data:
    print(x)

fruits = ["apple", "banana", "cherry"]
my_function(fruits)

for num in range(1, 11):
    print(num)

# 👇️ [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(range(1, 11)))
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

x = Student("Mike", "Olsen")
x.printname()

f = open("demofile.txt", "rt")
lines = f.readlines()
for line in lines:
 print(line, end="")

 f.close()
print("hiiii")
import os
os.remove("demofile.txt")

if 5%2!=0:
    print("weird")

import re

# All possible characters because \w does include _.
regex = re.compile(r'([0-9a-zA-Z])\1')

# Text
text = input()

# Search
matches = regex.search(text)

if matches:
    print(matches.group(1))
else:
    print(-1)