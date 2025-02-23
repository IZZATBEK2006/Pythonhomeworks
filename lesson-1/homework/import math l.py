homework L_1
# 1. Given a side of square. Find its perimeter and area.
def square_properties (side):
    perimeter = 4 * side 
    area = side ** 2
    return perimeter, area

#2. given diameter of circle. Find its lengths (circumference).
def circle_circumference (diameter):
    radius = diameter / 2
    circumference = 2 * math.pi * radius 
    return circumference

#3. Given two numbers a and b. Find their mean.
def mean(a, b):
    return (a+b) / 2

#4. Given two numbers a and b. Find their sum , product and square of each number.
def operations (a, b):
    sum_ab = a+b
    product_ab= a*b
    square_a = a ** 2
    square_b = b ** 2
    return sum_ab, product_ab, square_a, square_b