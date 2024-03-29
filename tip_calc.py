# Tip Calculator
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? "))
tip = int(input("How much tip would you like to give? "))
num_people = int(input("How many people to split the bill? "))

# per_person calcs bill divided by total # of people 
per_person = (bill // num_people)

# total_tip calcs total amount of tip to add to total of bill
total_tip = per_person * (1 + (tip / 100))

# prints the total amount w/tip to 2 decimal places
print(f"Each person should pay: {total_tip:.2f}.")

