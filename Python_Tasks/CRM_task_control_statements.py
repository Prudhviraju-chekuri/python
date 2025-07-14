""" Create a Python program to calculate discounts for 
customers based on their type, partnership duration, 
and deal stage using variables, conditionals, operators, 
and a case match statement. """
# CRM Task Requrequirements:
# Variables:
# customerId 
# customerName 
# isPremium (boolean – true for premium customers)
# yearsPartnership 
# dealStage (String – "Proposal", "Negotiation", "Closed")
# dealValue ( original value of the deal)

# Input variables
customer_id = input("Enter the customer id\n")
customer_name = input("Enter the customer name\n")
is_premium_input = input("Is a premium customer: Enter [Yes/No]\n")
is_premium = is_premium_input.strip().lower() == "yes"
years_partnership = int(input("Enter the no of years partnership\n"))
dealstage = input("Enter the deal stage: [Proposal/Negotiation/Closed]\n").strip().lower()
initial_deal_value = int(input("enter the deal value\n"))

# Conditional Statements:
# Apply a base discount based on customer type and partnership years:
# Premium customers: 10% discount.
# Non-premium with ≥3 years partnership: 5% discount.
# Others: 0% discount.

if is_premium:
    base_discount = 0.1
elif years_partnership >= 3:
    base_discount = 0.05
else:
    base_discount = 0.0

base_discount_percentage = int(base_discount * 100)

# case match Statement:
# Add an extra discount based on dealStage:
# "Proposal": +2%
# "Negotiation": +3%
# "Closed": +5%

match dealstage:
    case "closed":
        extra_discount = 0.05
    case "negotiation":
        extra_discount = 0.03
    case "proposal":
        extra_discount = 0.02
    case _:
        extra_discount = 0.0

extra_discount_percentage = int(extra_discount * 100)
total_discount_percentage = base_discount_percentage + extra_discount_percentage

# Calculation:
# Calculate the final discount and discounted deal value.
base_discount_value = base_discount * initial_deal_value
extra_discount_value = extra_discount * initial_deal_value
total_discount_value = base_discount_value + extra_discount_value
final_deal_value = initial_deal_value - total_discount_value

# Output
# Print customer details, base discount, extra discount, total discount, and final deal value.
print("\nCustomer Details:\n")
print(f"customer ID : {customer_id}")
print(f"customer name : {customer_name}")
print(f"Premium customer : {is_premium}")
print(f"Partenership Years : {years_partnership}")
print(f"Deal stage : {dealstage}")
print(f"Initail Deal Value : {initial_deal_value}")
print(f"{base_discount_percentage}% Base discount : {base_discount_value}")
print(f"{extra_discount_percentage}% Extra discount : {extra_discount_value}")
print(f"{total_discount_percentage}% Total discount : {total_discount_value}")
print(f"Final deal value : {final_deal_value}")








