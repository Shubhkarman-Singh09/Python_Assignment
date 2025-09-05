# 1. List operations
L = [11, 12, 13, 14]

# (i)
L.extend([50, 60])
print("After adding:", L)

# (ii)
for x in [11, 13]:
    if x in L:
        L.remove(x)
print("After removing:", L)

# (iii) Ascending
print("Ascending:", sorted(L))

# (iv) Descending
print("Descending:", sorted(L, reverse=True))

# (v) Search for 13
print("13 found?", 13 in L)

# (vi) Count elements
print("Count:", len(L))

# (vii) Sum
print("Sum:", sum(L))

# (viii) Sum of odd
print("Odd sum:", sum(x for x in L if x % 2 != 0))

# (ix) Sum of even
print("Even sum:", sum(x for x in L if x % 2 == 0))

# (x) Sum of prime
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
print("Prime sum:", sum(x for x in L if is_prime(x)))

# (xi) Clear elements
L.clear()
print("After clearing:", L)

# (xii) Delete list
del L
# print(L)   # would cause error

# -----------------------------------------------------

# 2. Sum list without inbuilt
lst = [2, 4, 6, 8]
s = 0
for i in lst:
    s += i
print("Manual Sum:", s)

# 3. Multiply list without inbuilt
p = 1
for i in lst:
    p *= i
print("Manual Product:", p)

# 4. 3*4*6 3D array
arr = [[['*' for k in range(6)] for j in range(4)] for i in range(3)]
print(arr)

# 5. Dictionary operations
D = {1:5.6, 2:7.8, 3:6.6, 4:8.7, 5:7.7}

D[8] = 8.8   # (i)
D.pop(2, None)   # (ii)
print("6 key present?", 6 in D)  # (iii)
print("Count:", len(D))  # (iv)
print("Sum of values:", sum(D.values()))  # (v)
D[3] = 7.1  # (vi)
D.clear()  # (vii)
print("After clear:", D)

# 6. Sets
S1 = {10, 20, 30, 40, 50, 60}
S2 = {40, 50, 60, 70, 80, 90}

S1.update([55, 66])  # (i)
S1 -= {10, 30}       # (ii)
print("40 present?", 40 in S1)  # (iii)
print("Union:", S1 | S2)  # (iv)
print("Intersection:", S1 & S2)  # (v)
print("S1 - S2:", S1 - S2)  # (vi)

# 7. Programs
import random, string

# (i) 100 random strings
for _ in range(100):
    ln = random.randint(6, 8)
    rand_str = ''.join(random.choice(string.ascii_letters) for i in range(ln))
    print(rand_str)

# (ii) Prime numbers between 600 and 800
primes = [n for n in range(600, 801) if is_prime(n)]
print("Primes 600-800:", primes)

# (iii) Divisible by 7 and 9
nums = [n for n in range(100, 1001) if n%7==0 and n%9==0]
print("Divisible by 7 & 9:", nums)

# 8. Examination schedule
exam_st_date = (11, 12, 2014)
print("Exam date: %i/%i/%i" % exam_st_date)

# 9. Divisible by 5
numbers = [10, 23, 45, 66, 90, 101]
for n in numbers:
    if n % 5 == 0:
        print(n)

# 10. Even/Odd with boolean
n = 17
is_even = (n % 2 == 0)
print("Even" if is_even else "Odd")

# 11. Count substring
text = "Emma is good. Emma likes coding. Emma is smart."
print("Occurrences of Emma:", text.count("Emma"))

# 12. Odd from list1, even from list2
list1 = [1,2,3,4,5,6,7]
list2 = [10,11,12,13,14,15]
new_list = [x for x in list1 if x%2!=0] + [y for y in list2 if y%2==0]
print("New list:", new_list)
