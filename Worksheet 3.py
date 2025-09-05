# 1. Difference with 17
def diff17(n):
    if n > 17:
        return abs(n - 17) * 2
    else:
        return 17 - n

print(diff17(22))  # Example
print(diff17(14))

# 2. Check range
def test_range(n):
    return (100 <= n <= 1000) or (n == 2000)

print(test_range(150))
print(test_range(2000))

# 3. Reverse string
def reverse_string(s):
    return s[::-1]

print(reverse_string("Python"))

# 4. Count upper and lower case
def count_case(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    return upper, lower

print(count_case("Hello World!"))

# 5. Distinct list elements
def distinct_list(lst):
    return list(set(lst))

print(distinct_list([1,2,2,3,4,4,5]))

# 6. Even numbers from list
def even_numbers(lst):
    return [x for x in lst if x % 2 == 0]

print(even_numbers([1,2,3,4,5,6,7,8,9]))

# 7. Function inside function
def outer_func():
    def inner_func():
        print("This is inside function")
    inner_func()

outer_func()

# 8. Function attributes
def student(name, roll, branch):
    return
print("Argument names:", student.__code__.co_varnames)

# 9. Student class with attributes
class Student:
    def __init__(self, student_id, student_name, student_class):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = student_class
    
    def display(self):
        print(f"ID: {self.student_id}, Name: {self.student_name}, Class: {self.student_class}")

s = Student(101, "Raj", "CSE")
s.display()

# 10. Student class with instances
class Student2:
    def __init__(self, sid, name, clas):
        self.sid = sid
        self.name = name
        self.clas = clas

student1 = Student2(1, "Aman", "ME")
student2 = Student2(2, "Rohit", "CSE")

for st in (student1, student2):
    print(f"ID: {st.sid}, Name: {st.name}, Class: {st.clas}")

# 11. Circle class
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

c = Circle(5)
print("Area:", c.area())
print("Perimeter:", c.perimeter())

# 12. String class
class StringClass:
    def __init__(self):
        self.str = ""
    
    def get_String(self):
        self.str = input("Enter a string: ")

    def print_String(self):
        print(self.str.upper())

sc = StringClass()
# sc.get_String()
# sc.print_String()
