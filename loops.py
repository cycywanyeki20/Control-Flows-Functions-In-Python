#PYTHON Loops are used to repeat a block of code multiple times. A process of iteration (repeating many times)
# There are two types of loops in Python:
# 1. For loop
# 2. While loop
# For loop is used to iterate over a sequence (like a list, tuple, dictionary, set, or string) or other iterable objects.
# The for loop in Python is used to iterate over a sequence (like a list, tuple, dictionary, set, or string) or other iterable objects.
subjects = ["Math", "Science", "English", "History"]
for subject in subjects:
 print(f"I love {subject}!")

#Loops in range
for number in range(16, 26):
    print(f"Number: {number}")

for number in range(1,15):
   print(f"Number:{number}")

# The while loop in Python is used to execute a block of code as long as the condition is true.
count = 1
while count <=5:
   print(f"count:{count}")
   count +=1

count = 5
while count >=5:
    print(f"count:{count}")
    count -=1

#Loop controls. Break and continue
# The break statement is used to exit a loop prematurely when a certain condition is met.
# The continue statement is used to skip the current iteration of a loop and move to the next iteration.
# The pass statement is a null operation; it does nothing when executed. It is used as a placeholder in loops, functions, classes, or conditionals.
for number in range (1,10):
   if number ==5:
      print("Breaking the loop at 5")
      break
   elif number % 2 == 0:
      print(f"skipping{number} because it is even")
      continue
   print(f"processing number:{number}")

   #Python Nested loops
# A nested loop is a loop inside another loop. The inner loop will be executed once for each iteration of the outer loop.
for i in range(3):
    for j in range(2):
        print(f"i:{i}, j:{j}")
    
            