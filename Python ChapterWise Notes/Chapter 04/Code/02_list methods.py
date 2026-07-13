L1 = [1, 8, 7, 21, 15, 2]

print(L1)

L1.count(8)                 # Counts how many times 8 appears
print(L1.count(8))

L1.index(21)                # Returns the index of 21
print(L1.index(21))

L1.extend([50, 60, 70])     # Adds multiple elements at the end
print(L1)

L2 = L1.copy()              # Creates a copy of the list
print(L2)

L2.clear()                  # Removes all elements from the list
print(L2)

print(len(L1))              # Returns total number of elements

print(max(L1))              # Returns the largest element

print(min(L1))              # Returns the smallest element

print(sum(L1))              # Returns the sum of all elements

print(sorted(L1))           # Returns a new sorted list (original unchanged)
print(L1)

print(list(reversed(L1)))   # Returns a reversed copy (original unchanged)
print(L1)

L1 += [100, 200]            # Adds multiple elements
print(L1)

L1 *= 2                     # Repeats the list twice
print(L1)

print(15 in L1)             # Checks if 15 exists
print(99 in L1)             # Checks if 99 exists

print(50 not in L1)         # Checks if 50 is not in the list

del L1[0]                   # Deletes element at index 0
print(L1)

del L1[1:4]                 # Deletes elements from index 1 to 3
print(L1)