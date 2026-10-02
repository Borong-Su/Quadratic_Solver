# Author: Borong SU
# Date: 24 September 2026
# Description: A simple program for calculating the roots of a quadratic equation.

import math

print("This is a tool for calculating the roots of a quadratic equation.")
print("It can solve an equation like: a*x^2 + b*x + c = 0")
print("Please enter the coefficients a, b, and c:")

a, b, c = map(int, input().split())

discriminant = b**2 - 4 * a * c

if discriminant < 0:
    print("There are no real roots.")
else:
    sqrt_discriminant = math.sqrt(discriminant)
    print("The first root is", (-b + sqrt_discriminant) / (2 * a))
    print("The second root is", (-b - sqrt_discriminant) / (2 * a))
