# SET BASICS
# Rules:
# 1. Unordered
# 2. No duplicate values
# 3. Mutable (add/remove allowed)
# 4. Defined using {}

# Example 1

numbers = {1, 2, 3, 2, 1}
print("Set (Duplicates Removed):", numbers)


# Example 2

colors = {"red", "blue"}
colors.add("green")      # adding element
colors.remove("blue")    # removing element

print("Updated Set:", colors)