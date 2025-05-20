#Good mastery of boolean functions and conditional statements is essential for programming.
temperature = 18

if temperature > 25:
    print("It's a hot day")
elif temperature < 10:
    print("It's a warm day")
else:
    print("It's a cold day")

    """
    Write an if/else/elif statement for a college with a grading system as shown below:
    If grade is 90 or higher, print A
    Else if grade is 80 or higher, print B
    Else if grade is 70 or higher, print C
    Else if grade is 60 or higher, print D
    Else print F
    """

grade = int(input("Enter your grade"))
if grade >= 90:
    print("A")
elif grade >=80:
    print("B")
elif grade >=70:
    print("C")
elif grade >=60:
    print("D")
else:
    print("F")