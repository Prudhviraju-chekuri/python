a = 4
b = 2
c = 12

d = 10

print(a+b)
print(a-b)
print(a/b)
print(a*b)
print(a**b)
print(a%b)

b += 2
print(b)
b-= 1
print(b)

is_equal = a==b
is_not_equal = a!=b
print(is_equal)
print(is_not_equal)
# Relational operators
str1 = "Python"
str2 = "Django"
str3 = "Django"

print(str1==str2)
print(str2==str3)
print(str1>str2)
print(str2>=str3)

# Logical operators
f =a>b
print(a>b and c>d)
print(not f)

# Membership operators
print("Membership operators")
txt = "Python is an programming language"

is_z_present = 'z' in txt
is_i_present = 'i' in txt
is_Python_present = "Python" in txt
is_pattern_present = "lang" in txt
is_java_not_present = "java" not in txt

print(is_z_present)
print(is_i_present)
print(is_Python_present)
print(is_pattern_present)
print(is_java_not_present)

 

course_list = ["Java", "Python", "cloud", "devops"]

in_python_present = "Python" in course_list
print(f"Is python present in the course list: {in_python_present}")

#Identity operators
# is , is not

num1 = 10
num2 = 10
num3 = 13

list1 = [1,2,3]
list2 = [1,2,3]
print(num1 is num2)
print(num2 is not num3)

print (list1 is list2)

# Bitwise operators
a = 10
b = 253

c= a & b
print(c)
c = a|b
print(c)

