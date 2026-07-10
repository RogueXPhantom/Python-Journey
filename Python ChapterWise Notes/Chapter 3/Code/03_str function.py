name = "harry"
print(len(name))

print(name.endswith("rry")) # Checks if the string ends with "rry"
print(name.startswith("har")) # Checks if the string starts with "har"
print(name.capitalize()) # Makes the first letter uppercase and the rest lowercase
print(name.upper()) # Converts all letters to uppercase
print(name.lower()) # Converts all letters to lowercase
print(name.find("rry")) # Returns the index of the first occurrence of "rry" in the string
print(name.replace("har", "par")) # Replaces "har" with "par" in the string
print(name.strip()) # Removes any leading and trailing whitespace from the string
print(name.lstrip()) # Removes any leading whitespace from the string
print(name.rstrip()) # Removes any trailing whitespace from the string
print(name.isdigit()) # Checks if the string consists only of digits
print(name.isalpha()) # Checks if the string consists only of alphabetic characters
print(name.count("r")) # Counts the number of occurrences of "r" in the string
print(name.index("r")) # Returns the index of the first occurrence of "r" in the string
print(name.isalnum()) # Checks if the string consists only of alphanumeric characters
print(name.islower()) # Checks if all the letters in the string are lowercase 
print(name.isupper()) # Checks if all the letters in the string are uppercase
print(name.swapcase()) # Swaps the case of all letters in the string (lowercase becomes uppercase and vice versa)
print(name.title()) # Converts the string to title case
print(name.center(10)) # Centers the string in a field of width 10
print(name.zfill(10)) # Pads the string with zeros on the left to make it 10 characters wide
print(name.split("r")) # Splits the string at each occurrence of "r"
print("-".join(name)) # Joins the characters of the string with "-"
print(name.partition("r")) # Partitions the string at the first occurrence of "r"
print(name.rfind("r")) # Returns the index of the last occurrence of "r" in the string
print(name.rindex("r")) # Returns the index of the last occurrence of "r" in the string
print(name.casefold()) # Converts all letters to lowercase
print(name.encode()) # Returns the encoded version of the string
print(name.expandtabs()) # Expands tabs in the string
print(name.removeprefix("ha")) # Removes the prefix "ha" from the string
print(name.removesuffix("ry")) # Removes the suffix "ry" from the string
print(name.isascii()) # Checks if all characters in the string are ASCII
print(name.isidentifier()) # Checks if the string is a valid identifier
print(name.ljust(10, "*")) # Left-justifies the string in a field of width 10, padding with "*"
print(name.rjust(10, "*")) # Right-justifies the string in a field of width 10, padding with "*"
print(name.zfill(8)) # Pads the string with zeros on the left to make it 8 characters wide