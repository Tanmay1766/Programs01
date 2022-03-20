import math
a=float(input("Enter side:"))
b=float(input("Enter side:"))
c=float(input("Enter side:"))
s=(a+b+c)/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area of Triangle:",area)
