"""
=================================================
LARGEST OF THREE NUMBERS
=================================================

Problem Statement:
Write a Python program to find the largest among three numbers.

-------------------------------------------------
Input Example:
10
45
23

Output Example:
45 is the largest number

-------------------------------------------------
Hints:
Use if-elif-else carefully.

=================================================
"""

# Write your code below this line

a = int(input())
b = int(input())
c = int(input())

if a >= b and a >= c:
    print(a, "is the largest number")

elif b >= a and b >= c:
    print(b, "is the largest number")

else:
    print(c, "is the largest number")

