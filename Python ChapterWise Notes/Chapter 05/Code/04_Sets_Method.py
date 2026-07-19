# Set Methods in Python

# Creating a set
s = {7, 8, 9, 2, 9, 2, 9, "Pulkit"}

# Note:
# Duplicate values are automatically removed.
print("Original Set:")
print(s)

# 1. add() - Adds one item
print()
print("1. add():")

s.add(10)
print(s)

# 2. update() - Adds multiple items
print()
print("2. update():")

s.update([11, 12, 13])
print(s)

# 3. remove() - Removes an item (gives an error if the item doesn't exist)
print()
print("3. remove():")

s.remove(8)
print(s)

# 4. discard() - Removes an item (no error if the item doesn't exist)
print()
print("4. discard():")

s.discard(100)
print(s)

# 5. pop() - Removes and returns a random item
print()
print("5. pop():")

removed_item = s.pop()

print("Removed Item:", removed_item)
print(s)

# 6. copy() - Creates a copy of the set
print()
print("6. copy():")

new_set = s.copy()

print(new_set)

# 7. union() - Combines two sets
print()
print("7. union():")

set2 = {20, 30, 40}

print(s.union(set2))

# 8. intersection() - Returns common items
print()
print("8. intersection():")

set3 = {7, 10, 20}

print(s.intersection(set3))

# 9. difference() - Returns items present only in the first set
print()
print("9. difference():")

print(s.difference(set3))

# 10. symmetric_difference() - Returns items that are not common
print()
print("10. symmetric_difference():")

print(s.symmetric_difference(set3))

# 11. issubset() - Checks if one set is inside another
print()
print("11. issubset():")

small_set = {7, 10}

print(small_set.issubset(s))

# 12. issuperset() - Checks if a set contains another set
print()
print("12. issuperset():")

print(s.issuperset(small_set))

# 13. isdisjoint() - Checks if two sets have no common items
print()
print("13. isdisjoint():")

set4 = {100, 200}

print(s.isdisjoint(set4))

# 14. clear() - Removes all items
print()
print("14. clear():")

new_set.clear()

print(new_set)

# Output:
# set()