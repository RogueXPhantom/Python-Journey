name = "harry"

# ==========================
# 1. len()
# Counts the total number of characters.
print(len(name))
# Result: 5

# ==========================
# 2. endswith()
# Checks if the string ends with the given text.
print(name.endswith('rry'))
# Result: True

# ==========================
# 3. startswith()
# Checks if the string starts with the given text.
print(name.startswith('har'))
# Result: True

# ==========================
# 4. capitalize()
# Makes the first letter uppercase.
print(name.capitalize())
# Result: Harry

# ==========================
# 5. upper()
# Converts all letters to uppercase.
print(name.upper())
# Result: HARRY

# ==========================
# 6. lower()
# Converts all letters to lowercase.
print(name.lower())
# Result: harry

# ==========================
# 7. find()
# Returns first index or -1 if not found.
print(name.find('rry'))
# Result: 2

# ==========================
# 8. replace()
# Replaces text.
print(name.replace('har','par'))
# Result: parry

# ==========================
# 9. strip()
# Removes spaces from both ends.
print(name.strip())
# Result: harry

# ==========================
# 10. lstrip()
# Removes spaces from the left.
print(name.lstrip())
# Result: harry

# ==========================
# 11. rstrip()
# Removes spaces from the right.
print(name.rstrip())
# Result: harry

# ==========================
# 12. isdigit()
# Checks if all characters are digits.
print(name.isdigit())
# Result: False

# ==========================
# 13. isalpha()
# Checks if all characters are letters.
print(name.isalpha())
# Result: True

# ==========================
# 14. count()
# Counts occurrences of text.
print(name.count('r'))
# Result: 2

# ==========================
# 15. index()
# Returns first index or raises an error.
print(name.index('r'))
# Result: 2

# ==========================
# 16. isalnum()
# Checks if only letters and digits exist.
print(name.isalnum())
# Result: True

# ==========================
# 17. islower()
# Checks if all letters are lowercase.
print(name.islower())
# Result: True

# ==========================
# 18. isupper()
# Checks if all letters are uppercase.
print(name.isupper())
# Result: False

# ==========================
# 19. swapcase()
# Swaps uppercase and lowercase.
print(name.swapcase())
# Result: HARRY

# ==========================
# 20. title()
# Capitalizes the first letter of every word.
print(name.title())
# Result: Harry

# ==========================
# 21. center()
# Centers the string in the given width.
print(name.center(10))
# Result: '  harry   '

# ==========================
# 22. zfill()
# Pads the left with zeros.
print(name.zfill(10))
# Result: 00000harry

# ==========================
# 23. split()
# Splits the string into a list.
print(name.split('r'))
# Result: ['ha', '', 'y']

# ==========================
# 24. join()
# Joins characters using a separator.
print('-'.join(name))
# Result: h-a-r-r-y

# ==========================
# 25. partition()
# Splits into before, separator and after.
print(name.partition('r'))
# Result: ('ha', 'r', 'ry')

# ==========================
# 26. rfind()
# Returns the last index or -1.
print(name.rfind('r'))
# Result: 3

# ==========================
# 27. rindex()
# Returns the last index or raises an error.
print(name.rindex('r'))
# Result: 3

# ==========================
# 28. casefold()
# Converts to lowercase for comparisons.
print(name.casefold())
# Result: harry

# ==========================
# 29. encode()
# Converts the string into bytes.
print(name.encode())
# Result: b'harry'

# ==========================
# 30. expandtabs()
# Replaces tabs with spaces.
print(name.expandtabs())
# Result: harry

# ==========================
# 31. removeprefix()
# Removes the given prefix.
print(name.removeprefix('ha'))
# Result: rry

# ==========================
# 32. removesuffix()
# Removes the given suffix.
print(name.removesuffix('ry'))
# Result: har

# ==========================
# 33. isascii()
# Checks if all characters are ASCII.
print(name.isascii())
# Result: True

# ==========================
# 34. isidentifier()
# Checks if it's a valid variable name.
print(name.isidentifier())
# Result: True

# ==========================
# 35. ljust()
# Pads the right side.
print(name.ljust(10,'*'))
# Result: harry*****

# ==========================
# 36. rjust()
# Pads the left side.
print(name.rjust(10,'*'))
# Result: *****harry

# ==========================
# 37. zfill()
# Pads the left with zeros to width 8.
print(name.zfill(8))
# Result: 000harry

