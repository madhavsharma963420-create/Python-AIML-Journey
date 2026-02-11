# Basic Input Example

name = input("Enter your name: ")
print("Hello", name)

# Input with Type Conversion

age = int(input("Enter your age: "))
marks = float(input("Enter your marks: "))

print("Your age is:", age)
print("Your marks are:", marks)

# Multiple Input in One Line

a, b = map(int, input("Enter two numbers separated by space: ").split())

print("First number:", a)
print("Second number:", b)
print("Sum:", a + b)

