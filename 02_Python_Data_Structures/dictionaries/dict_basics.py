# DICTIONARY BASICS
# Rules:
# 1. Key-Value pairs
# 2. Keys must be unique
# 3. Mutable (update possible)
# 4. Defined using {}

# Example 1

student = {
    "name": "Madhav",
    "age": 21,
    "course": "AIML"
}

print("Student Name:", student["name"])
print("Student Age:", student["age"])


# Example 2 - Updating value

student["age"] = 22
student["college"] = "XYZ University"

print("Updated Dictionary:", student)