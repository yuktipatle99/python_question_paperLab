# Q8: Set Operations in Python

A = {1, 2, 3, 4}
B = {2, 3, 5}

print(A & B)
print(A | B)
print(A - B)
print(A ^ B)
print({1, 2} <= {1, 2, 3})

# Dictionary with list as a key
# print({[1, 2, 3]: 'abc'})  # Raises TypeError

# Dictionary with tuple as a key
print({(1, 2, 3): 'abc'})