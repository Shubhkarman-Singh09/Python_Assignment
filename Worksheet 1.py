# 1. Print a specific formatted string
print("""Twinkle, twinkle, little star,
    How I wonder what you are!
        Up above the world so high,
        Like a diamond in the sky.
Twinkle, twinkle, little star,
    How I wonder what you are""")

# 2. Reverse first and last name
first = input("Enter first name: ")
last = input("Enter last name: ")
print(last + " " + first)

# 3. Area of circle
import math
r = float(input("Enter radius: "))
area = math.pi * r * r
print("Area of circle:", area)

# 4. First and last colors
color_list = ["Red","Green","White" ,"Black"]
print(color_list[0], color_list[-1])

# 5. Compute n + nn + nnn
n = int(input("Enter number: "))
print(n + int(str(n)*2) + int(str(n)*3))

# 6. List and tuple from input
nums = input("Enter comma-separated numbers: ")
lst = nums.split(",")
tpl = tuple(lst)
print("List:", lst)
print("Tuple:", tpl)

# 7. Celsius to Fahrenheit
c = float(input("Enter temperature in Celsius: "))
f = (c * 9/5) + 32
print("Temperature in Fahrenheit:", f)

# 8. Swap two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
a, b = b, a
print("After swapping:", a, b)

# 9. Odd or Even
n = int(input("Enter a number: "))
print("Even" if n % 2 == 0 else "Odd")

# 10. Leap year check
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

# 11. Euclidean distance
import math
x1, y1 = map(float, input("Enter first point (x1 y1): ").split())
x2, y2 = map(float, input("Enter second point (x2 y2): ").split())
dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
print("Euclidean Distance:", dist)

# 12. Triangle validity
a, b, c = map(int, input("Enter three angles: ").split())
if a+b+c == 180 and a>0 and b>0 and c>0:
    print("Valid Triangle")
else:
    print("Not a Triangle")

# 13. Compound Interest
p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time in years: "))
ci = p * (pow((1 + r/100), t)) - p
print("Compound Interest:", ci)

# 14. Prime check
n = int(input("Enter a number: "))
if n > 1:
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")

# 15. Sum of squares
N = int(input("Enter number N: "))
total = sum(i**2 for i in range(1, N+1))
print("Sum of squares:", total)
