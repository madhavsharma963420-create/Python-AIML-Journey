# Remove duplicates from list using set

numbers = [1, 2, 2, 3, 4, 4, 5]

unique_numbers = list(set(numbers))

print("Original List:", numbers)
print("Unique List:", unique_numbers)


# Convert tuple to list and modify

data = (10, 20, 30)

data_list = list(data)
data_list.append(40)

print("Original Tuple:", data)
print("Modified List:", data_list)


# Count frequency of characters

word = "programming"

frequency = {}

for char in word:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print("Character Frequency:", frequency)


# Find common elements between two lists

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

common = set(list1) & set(list2)

print("Common Elements:", common)


# Create dictionary from two lists

names = ["Aman", "Rahul", "Madhav"]
marks = [75, 82, 90]

student_dict = dict(zip(names, marks))

print("Student Dictionary:", student_dict)


# Find student with highest marks

students = {
    "Aman": 75,
    "Rahul": 82,
    "Madhav": 90
}

topper = max(students, key=students.get)

print("Topper:", topper)
print("Marks:", students[topper])


