# LIST PRACTICE PROGRAMS

# Example 1 - Sum of elements

numbers = [10, 20, 30, 40]

total = 0
for num in numbers:
    total += num

print("Sum of List:", total)


# Example 2 - Find Maximum element

nums = [5, 12, 7, 3]

maximum = nums[0]

for n in nums:
    if n > maximum:
        maximum = n

print("Maximum Value:", maximum)