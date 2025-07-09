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
print(msg1+msg2+msg3+version)