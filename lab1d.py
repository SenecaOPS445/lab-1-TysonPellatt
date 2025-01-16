#!/usr/bin/env python3
'''
print(10 + 5)   # addition
print(10 - 5)   # subtraction
print(10 * 5)   # multiplication
print(10 / 5)   # division
print(10 ** 5)  # exponenets

print(10 + 5 * 2)          # multpicaion happend before addition
print((10 + 5) * 2)        # parentheses happen before multplication
print(10 +5 * 2 - 10 **2)  # first exponents, then multplication, then addition and subtraction form left-to right
print(15 / 3 * 4)          # division and multiplication happend from left-to right
print(100 / ((5 + 5) * 2)) # the inner most parentheses are first preforming additon, then parentheses again with multiplication, finally the division
'''

x = 10
y = 2
z = 5
result = (x + y * z)
print(f"{x} + {y} * {z} = {result}")
