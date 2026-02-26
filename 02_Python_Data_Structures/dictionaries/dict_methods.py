# DICTIONARY METHODS

# Example 1 - keys(), values(), items()

student = {
    "name": "Madhav",
    "age": 21,
    "course": "AIML"
}

print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())


# Example 2 - pop(), get()

student.pop("age")   # removes key
print("After Pop:", student)

print("Get Method:", student.get("name"))