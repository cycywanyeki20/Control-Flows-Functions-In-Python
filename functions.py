#Python functions allow you to define reusable blocks of code that can be called with different arguments.
# Functions help to organize code, improve readability, and reduce redundancy.
# Functions can take parameters (inputs) and return values (outputs).
#positional arguments
def add(a, b):
    return(a + b)
print(add(3, 6))

#Default arguments
def greet (name="Guest"):
    return f"Hello,{name}!"
print(greet())
print(greet("Alice"))

def fruits (name="Mango"):
    return f"red, {name}!"
print(fruits())
print(fruits("Banana"))

#Keyword arguments
def introduce (name, age):
    return f"My name is {name}, and I am {age} years old."
print(introduce(age=25, name="Cycy"))

def introduce (name, age, career, location):
    return f"My name is {name}, I am a {age} year old {career} from {location}."
print(introduce(age=24, name='Cycy', career='Data Scientist', location='Nairobi,Kenya'))

#Returning Values
def square(number):
    return number**2
result = square(5)
print(result)

#Lambda Functions. Python supports anonymous functions using lambda keyword. Useful for short simple functions.
add = lambda x,y: x+y
print(add(3,5))

#Using Lmbda with map()
numbers = [1,2,3,4]
squares = list(map(lambda x: x**2, numbers))
print(squares)

#Recursive Functions. A function can call itself enablingnrecursive problem-solving.
def factorial(n):
    if n ==1:
        return 1
    return n*factorial(n-1)
print(factorial(5))