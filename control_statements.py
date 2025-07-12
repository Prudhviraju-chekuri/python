# Decision making statement
# if statement
x = 6
list1 = [1,2,3,4,5]
if x in list1 :
    print("if block is executed")

else :
    print("else block")

num = 128

if num>=10 and num<=20 :
    print(f"{num} is in Range 10-20")
elif num<10:
    print(f"{num} is left out of range")
elif num>20:
    print(f"{num} is right out of range")
else:
    print(f"{num} is not in the range 10-20")# this never get executed

# vote application




# input funtion demo
name = input("Enter your name\n")
print(f"welcome {name}")
age = int(input("Enter your age\n")) # need to type cast from string to int
if age>=18:
    print("you can vote")
else:
    print("you are not allowed to vote")

# ternary operator
# value_if_true if condition else value_if_false
print("you can vote") if age>=18 else print("you are not allowed to vote")

#elif ladder
marks = int(input("Enter you marks\n"))
if marks>75:
    print("Grade A")
elif marks>= 60:
    print("Grade B")
elif marks>=50:
    print("Grade c")
else:
    print("Idiot you got Failed")

# vote app with ID card

age = int(input("Enter your age\n")) # need to type cast from string to int
id_input = input("Do you have ID card [Y/N]\n")
has_id = True if id_input == "Y" else False
if age>=18:
    if has_id:
        print("You can vote")
    else:
        print("You need ID card to vote")
else:
    print("You cannot vote")

