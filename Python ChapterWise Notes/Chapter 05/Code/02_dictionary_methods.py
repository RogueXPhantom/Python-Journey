# Dictionary Methods in Python

# Creating a dictionary
marks = {
    "harry": 100,
    "shubham": 56,
    "rohan": 23
}

# 1. items() - Returns all key-value pairs
print("1. items():")
print(marks.items())

# Output:
# dict_items([('harry', 100), ('shubham', 56), ('rohan', 23)])


# 2. keys() - Returns all keys
print()
print("2. keys():")
print(marks.keys())

# Output:
# dict_keys(['harry', 'shubham', 'rohan'])


# 3. values() - Returns all values
print()
print("3. values():")
print(marks.values())

# Output:
# dict_values([100, 56, 23])


# 4. get() - Returns the value of the given key
print()
print("4. get():")

print(marks.get("harry"))   # Key exists
# Output: 100

print(marks.get("rahul"))   # Key does not exist
# Output: None

# Note:
# get() returns None if the key is not found.
# It does NOT give an error.


# 5. update() - Changes the value of a key or adds a new key
print()
print("5. update():")

marks.update({"harry": 90})
print(marks)

# Output:
# {'harry': 90, 'shubham': 56, 'rohan': 23}

# Adding a new key
marks.update({"aman": 75})
print(marks)

# Output:
# {'harry': 90, 'shubham': 56, 'rohan': 23, 'aman': 75}

# Note:
# update() changes the dictionary directly.
# It does not return anything.


# 6. pop() - Removes a key and returns its value
print()
print("6. pop():")

removed = marks.pop("rohan")

print("Removed Value:", removed)
print("Dictionary:", marks)

# Output:
# Removed Value: 23
# Dictionary:
# {'harry': 90, 'shubham': 56, 'aman': 75}


# 7. popitem() - Removes the last inserted key-value pair
print()
print("7. popitem():")

last_item = marks.popitem()

print("Removed Item:", last_item)
print("Dictionary:", marks)

# Output:
# Removed Item: ('aman', 75)
# Dictionary:
# {'harry': 90, 'shubham': 56}


# 8. setdefault() - If the key exists, returns its value.
# If it doesn't exist, adds the key with the given value.
print()
print("8. setdefault():")

print(marks.setdefault("aman", 80))

# Since "aman" doesn't exist now, it will be added.
print(marks)

# Output:
# 80
# {'harry': 90, 'shubham': 56, 'aman': 80}


# 9. copy() - Creates a copy of the dictionary
print()
print("9. copy():")

new_marks = marks.copy()

print(new_marks)

# Output:
# {'harry': 90, 'shubham': 56, 'aman': 80}


# 10. fromkeys() - Creates a new dictionary using given keys
print()
print("10. fromkeys():")

students = dict.fromkeys(["A", "B", "C"], 0)

print(students)

# Output:
# {'A': 0, 'B': 0, 'C': 0}


# 11. clear() - Removes all items from the dictionary
print()
print("11. clear():")

new_marks.clear()

print(new_marks)

# Output:
# {}