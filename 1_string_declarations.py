"""
String declarations
"""

# Single quotes
string1 = 'Hello, World!'
print(string1)

# Double quotes
string2 = "Hello, World!"
print(string2)

# Triple quotes
string3 = '''Hello, World!'''

# Triple quotes can be used for multi-line strings
string4 = '''Hello,
World!'''

# This is useful for docstrings which are used to document functions


# Concatenation
string5 = 'Hello, ' + 'World!'
print(string5)
#Notice the space after the comma.

# Repetition. Strings can be repeated using operators such as '*'
string6 = 'Hello, ' * 3
print(string6)

# Strings can be indexed by letter positions. Indexing starts at 0.
# This will come up later when we will talk about lists.
string7 = 'Hello, World!'
print(f"Printing string7[0]: {string7[0]}")
print(f"Printing string7[1]: {string7[1]}")
print(f"Printing string7[2]: {string7[2]}")
print(f"Printing string7[3]: {string7[3]}")
print(f"Printing string7[4]: {string7[4]}")
print(f"Printing string7[5]: {string7[5]}")
print(f"Printing string7[6]: {string7[6]}")
print(f"Printing string7[7]: {string7[7]}")
#And so on...

#Strings are immultable, which means that they cannot be changed.
#string7[0] = 'h' <This would raise an error.
#String item does not support item assignment.
# This, howver, does not mean that you cannot reassign them.
string7 = "I have been reassigned"
print(string7)
#It simply means that its conents cannot be changed.
#Next we will talk about integers!

