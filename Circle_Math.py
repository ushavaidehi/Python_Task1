from math import pi

# Math_Circle

r = float(input("Radius: "))

print("Area of the Circle is: " + str(pi*r**2))
print("Diameter of the Circle is: " + str(2*r))
print("Circumference of the Circle is: " + str(2*pi*r))

print()
# Math_Square
import math
s = float(input("Side: "))
print("Area of square is: " + str(s*s))
print ("Diagonal of the Square is: " + str(math.sqrt(2)*s))
print ("Perimeter of the Square is: " + str(4*s))

print()
# Math_Rectangle

w = float(input("Width of the rectangle is: "))
l = float(input("Length of the rectangle is: "))
d = print("Diagonal of the rectangle is: " + str(math.sqrt(w**2+l**2)))
p = print("Perimeter of the rectangle is: " + str(2*l+2*w))
ar = print("Area of the rectangle is: " + str(w*l))


print()
# Math_Triangle

sa = int(input("Side A of the Triangle is: "))
sb = int(input("Side B of the Triangle is: "))
sc = int(input("Side C of the Triangle is: "))
th = print("Height of the triangle is: " + str(2*sa/sb))

# Perimeter

tp = int(sa) + int(sb)+ int(sc)
print("Perimeter of the triangle is: ", tp)

# Base

tb = int(tp) - int(sa) - int(sc)
print("Base of the triangle is: ", tb)














