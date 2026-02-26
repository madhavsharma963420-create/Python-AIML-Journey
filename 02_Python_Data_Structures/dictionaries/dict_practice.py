# DICTIONARY PRACTICE PROGRAMS

# Example 1 - Count frequency of elements in a list

numbers = [1, 2, 2, 3, 3, 3, 4]

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print("Frequency Count:", frequency)


# Example 2 - Find student with highest marks

students = {
    "Rahul": 75,
    "Aman": 82,
    "Madhav": 90,
    "Riya": 85
}

highest = max(students, key=students.get)

print("Topper:", highest)
print("Marks:", students[highest])