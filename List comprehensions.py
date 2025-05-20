#An elegant way to create and manipulate lists in Python is through list comprehensions.
# List comprehensions provide a concise way to create lists based on existing lists or other iterable objects.
squares =[]
for x in range (5):
    squares.append(x**2)
squares = [x**2 for x in range(5)]
print(squares)
# The above code creates a list of squares of numbers from 0 to 4 using a list comprehension.

squares =[]
for j in range(10):
    squares .append(x**2)
squares= [x**2 for x in range(10)]
print(squares)

#Nested List Comprehensions
#3X3 MATRIX using nested list comprehensions
matrix =[i*j for j in range(1,4) for i in range(1,4)]
print(matrix)

#list compregension with a condition
even_numbers= [x  for x in range(10) if x % 2  ==0]
print(even_numbers)

#Transforming data with list comprehensions
fruits =["apple","banana","Mango"]
# Convert all fruits to uppercase
fruits_fruits = [fruit.upper()for fruit in fruits]
print(fruits_fruits)

#Filtering data with list comprehensions
numbers=[10,15,25,30,20]
divisible_by_5 = [num for num in numbers if num % 5 == 0]
print(divisible_by_5)

for number in range(1,50):
    if number % 5 == 0:
        print(f"{number} is divisible by 5")

#flatening a list
nested_list =[[1,2],[3,4],[5,6]]
flattened_list = [item for sublist in nested_list for item in sublist]
print(flattened_list)

#Complex lists
result =[x*y for x in range(10) for y in range(5) if x+y>5]
print(result)