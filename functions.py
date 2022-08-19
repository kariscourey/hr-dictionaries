# verify_age(customer_one_age) # doesn't work here

def verify_age(age):
    if age > 17:
        print(f"{age} is old enough to buy a lottery ticket.")
        # print("How many would you like?")
    else:
        print(f"{age} is not old enough to buy a lottery ticket.")
        # print("Can I interest you in some candy?")
    print("Thank you for your patronage.")

def verify_interest(interest):
    if interest == True:
        print("Excellent choice, but we only have Twix.")
        print("How many would you like? ")
    else:
        print("Come back another time!")
    print("Thank you for your patronage.")

# verify_age(customer_one_age) # doesn't work here

# print(customer_one_age)
customer_one_age = 23
customer_two_age = 16
customer_three_age = 17
customer_four_age = 25
customer_one_interest = True

verify_age(customer_two_age)
verify_interest(customer_one_interest)
