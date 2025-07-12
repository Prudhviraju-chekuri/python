# Strings Methods
# 1. Check string content

""" user_input = input("Enter your name\n")
if user_input.isalpha():
    print(f"{user_input} is alphabetic strings")
    if user_input.islower():
        print(f"{user_input} is in lower case")
    elif user_input.isupper():
        print(f"{user_input} is in upper case")
    elif user_input.istitle():
        print(f"{user_input} is in title case")
    print(f"user input is coverted to {user_input.lower()}")
    print(f"user input is coverted to {user_input.upper()}")
    print(f"user input is coverted to {user_input.title()}")
    print(f"user input is coverted to {user_input.capitalize()}")
    print(f"user input is coverted to {user_input.swapcase()}")
elif user_input.isdigit():
    print(f"{user_input} contains only digits")
elif user_input.isalnum():
    print(f"{user_input} is alphanumeric")
elif user_input.isspace():
    print(f"{user_input} is all white spaces")
    print(f"user input is coverted to {user_input.lower()}")
    print(f"user input is coverted to {user_input.upper()}")
    print(f"user input is coverted to {user_input.title()}")
    print(f"user input is coverted to {user_input.capitalize()}")
    print(f"user input is coverted to {user_input.swapcase()}")
else:
    print("Invalid entry")
print(f"user input is coverted to {user_input.lower()}")
print(f"user input is coverted to {user_input.upper()}")
print(f"user input is coverted to {user_input.title()}")
print(f"user input is coverted to {user_input.capitalize()}")
print(f"user input is coverted to {user_input.swapcase()}")

updated_string = user_input.strip()
print(f"strip updated string is {updated_string}")
updated_string = user_input.lstrip()
print(f"lstrip updated string is {updated_string}")
updated_string = user_input.rstrip()
print(f"rstrip updated string is {updated_string}") """

# find
string = input("Enter the input string\n")
# finding_string = input("Enter the string to find\n")
#index = string.find(finding_string)
#if index == -1:
#    print(f"{finding_string} is not found in {string}")
#else:
#    print(f"{finding_string} is fount at {index} index")

#index = string.index(finding_string)
#print(f"{finding_string} is fount at {index} index")
""" prefix_string = input("Enter the prefix string\n")
if string.startswith(prefix_string):
    print(f"{string} starts with {prefix_string}")
else:
    print(f"{string} doesn't starts with {prefix_string}") """

""" suffix_string = input("Enter the sufix string\n")
if string.endswith(suffix_string):
    print(f"{string} ends with {suffix_string}")
else:
    print(f"{string} doesn't end with {suffix_string}") """

""" counting_string = input("Enter the counting string\n")
count_number = string.count(counting_string)
if count_number == 0:
    print(f"{counting_string} is not present in {string}")
else:
    print(f"{counting_string} is present in {string} {count_number} times") """

split_output = string.rsplit()
print(split_output)





