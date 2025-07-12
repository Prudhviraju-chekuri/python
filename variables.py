# Syntax
# variable_name = value
# = Assignment operator

value_num = 10
value_rating = 4.2
value_name = "Prudhvi"
value_rating_new = 4.2
print(id(value_num)) # unique identity i.e memory address
print(id(value_rating))
print(id(value_name))
print(id(value_rating_new)) # Immutable data value_rating & value_rating_new has same address

# Mutable Data

list1 =[1,2,3]
list2 =[1,2,3]

print(id(list1))
print(id(list2))

print(type(value_num))
print(type(value_rating))
print(type(value_name))

# output variables

msg = "Python is awsome"
print(msg)

#concatenation
msg1 = "Python "
msg2 = "is "
msg3 = "Awsome"

print(msg1+msg2+msg3)
version =3
#print(msg1+msg2+msg3+version) cannot concatenate string with number
version  = "3"
print(msg1+msg2+msg3+version) # valid

print(msg,version) # valid concatenation using , separator

# many values to multiple variables

x,y,z = "Python", "Is", "Awsome"
print(x)
print(x,y,z)

# one value to multiple variables
x = y = z = "Python"
print(x,y,z)

# ProductName ---> Pascal case (class name)

# productName ---> Camel case (Objectname)

# product_name ---> Snake Case (when using variable & functions)

product_brand = "Levis"
product_rating = 4.2
product_price = 1600

airbag_present = True

# Prepare variables for cardekho.py
# https://www.cardekho.com/hyundai/creta/specs

print(type(product_brand))
print(type(product_rating))
print(type(product_price))

name = "Prudhvi"
session = 9
print(f"My name is :{name} and session is at :{session}", f"How are you {name}")
print(f"i am {name} and my session is at {session}")