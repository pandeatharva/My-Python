# print("Hello World!");

Fname = "Tony"
Lname = "Stark"
Age = 51
Is_genius = True

#name = input("What is your name?")
#print(name)

#Sname = input("What is your super hero name?")
#print(Sname)

#old_age = input("What is your age? ")
#age = int(old_age) + 2
#print(age)

#first = input("Enter first number: ")
#second = input("Enter second number: ")
#sum = int(first) + int(second)
#print(sum)
""""
age = int(input("Enter age: "))

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

"""

# Calculator project
""""
firstno = input("Enter first number: ")
operator = input("Enter operator (+,-,*,/,%): ")
secondno = input("Enter second number: ")

firstno = int(firstno)
secondno = int(secondno)

if operator == '+':
    print(firstno + secondno)

elif operator == '-':
    print(firstno - secondno)

elif operator == '*':
    print(firstno * secondno)

elif operator == '/':
    print(firstno / secondno)

elif operator == '%':
    print(firstno % secondno)

else:
    print("Invalid operation")

"""
# Loops
"""
i = 5
while i >= 1:
    print(i * "*")
    i -= 1

for i in range(7):
    print(i + 1)

"""
"""

marks = [19, 20, 16, 18,15]
print(marks[1:3])
marks.insert(1, (18))
print(marks)
print(10 in marks)
print(len(marks))

i = 0
while i < len(marks):
    print(marks[i])
    i = i + 1

"""

"""
students = ["ram", "shaym", "sai", "radha", "sita"]

for student in students:
    if student == "sai":
        continue;
    print(student)

marks = {"english": 16, "maths": 19, "science":18 }
print(marks["maths"])


def print_sum (first, second= 8):
    print(first + second)

print_sum(4)
"""

"""
name = input("Enter name: ")
print("Good morning,", name)

letter = '''Dear <|NAME|>,
 You are selected!
 Date: <|DATE|>
 '''

name = input("Enter name ")
date = input("Enter date ")

letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter)

"""

"""
# Basic Calculator

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

sum = int(num1) + int(num2)
diff = int(num1) - int(num2)

print(sum, diff)

"""

"""
# Tuple
coordinates = (3,5,7,0,4,(5,5),(7,7,7))
print(coordinates)

"""

"""
#Functions

def sayhello(name):
    print("Hello " + name +"!")

sayhello("Mike")

def cube(num):
    return num*num*num

print(cube(3))
"""

"""
# Better calculator

num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1 - num2)
elif op == '*':
    print(num1 * num2)
elif op == '/':
    print(num1 / num2)
else:
    print("Invalid operator")

"""

"""
# Guessing game

secret_word = "Man"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess!= secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of guesses, You lose!")
else:
    print("You win!")
    
"""
"""
friends = ['Akshay', 'PJD', 'Bhangi']

for friend in friends:
    print(friend)
"""

"""
# Power function

def raise_to_pow(base_num, pow_num):
    result = 1
    for i in range(pow_num):
        result = result * base_num

    print(result)

raise_to_pow(2, 5)

"""

"""
# Translation

# Any vowel changes to 's'

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            if letter.isupper():
                translation = translation + 'S'
            else:
                translation = translation + 's'
        else:
            translation = translation + letter

    return translation

print(translate(input("Enter phrase: ")))

"""

try:
    number = int(input("Enter a number: "))
    print(number)
except:
    print("Invalid input")
