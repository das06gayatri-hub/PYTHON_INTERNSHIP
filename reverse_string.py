"""
=================================================
REVERSE A STRING
=================================================

Problem Statement:
Write a Python program to reverse a string.

-------------------------------------------------
Instructions:
1. Take string input from the user.
2. Reverse the string using:
   - slicing AND
   - loop
3. Print reversed string.

-------------------------------------------------
Input Example:
Python

Output Example:
nohtyP

-------------------------------------------------
Expected Concepts:
- string slicing
- loops
- indexing

=================================================
"""

# Write your code below this line
-Using Slicing 
s = input("Enter a string: ")
rev = s[::-1]

print("Reversed string:", rev)

-Using loop
s = input("Enter a string: ")

rev = ""
for a in s:
    rev = a + rev

print("Reversed string:", rev)
