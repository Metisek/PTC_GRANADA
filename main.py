import os
import glob
import importlib.util
import sys
import ex1, ex2, ex3, ex4, ex5, ex6, ex7, ex8


# Exercise 1
ex1solve = ex1.solve(2, 3)
max_val, min_val = ex1solve[0], ex1solve[1]
print('MAX: {}, MIN: {}'.format(max_val, min_val))

# Exercise 2
h1, m1, s1 = 12, 30, 15
h2, m2, s2 = 14, 45, 30
print('Time difference in seconds: {}'.format(ex2.solve(h1, m1, s1, h2, m2, s2)))

# Exercise 3
time1 = "12:30:15"
time2 = "14:45:30"
print('Time difference in time format: {}'.format(ex3.solve(time1, time2)))

# Exercise 4
price = 3.75
print('Minimum amount of refunded coins in price {}: {}'.format(price, ex4.solve(price)))

# Exercise 5
range1 = 2
range2 = 4.2
print('Sum of numbers in closed range between {} and {}: {}'.format(range1, range2, ex5.solve(range1, range2)))

# Exercise 6
n = 5
k = 2
print('Combinatorio form n = {} and k = {}: {}'.format(n, k, ex6.solve(n, k)))

# Exercise 7
num = 1234
print('First value smaller than given number: {} that is diviseable by 9: {}'.format(num, ex7.solve(num)))

# Exercise 8
year1 = 2021
year2 = 2000

print('Nearest leap year to {} is: {}'.format(year1, ex8.solve(year1)))
print('Nearest leap year to {} is: {}'.format(year2, ex8.solve(year2)))