# LIST BASICS
# Rules:
# 1. Ordered
# 2. Mutable (change ho sakti hai)
# 3. Duplicate values allowed
# 4. Defined using []

# Example 1

numbers = [10, 20, 30, 40]
print("Original List:", numbers)

print("First Element:", numbers[0])
print("Last Element:", numbers[-1])


# Example 2

fruits = ["apple", "banana", "apple"]
print("Duplicates Allowed:", fruits)

fruits[1] = "mango"   # updating value
print("After Update:", fruits)