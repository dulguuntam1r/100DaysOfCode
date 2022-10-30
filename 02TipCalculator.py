#Second day challenge
#Apply tip (as percentage) to the bill and divide it equally among number of people present

print("Welcome to the tip calculator!\n")
bill_amount = float(input("What was the total bill?\n$"))
tip_percentage = int(input("What percentage tip would you like to give?\n")) / 100 + 1
number_of_people = int(input("How many people to split the bill?\n"))

#Calculating the bill and rounding the float numbers to 2 but this doesn't show 2 float numbers if it ends with 0
bill_per_person = round(bill_amount * tip_percentage / number_of_people, 2)

#Format the final value to show 2 floating numbers even if its zero
formatted_bill_per_person = "{:.2f}".format(bill_per_person)

print(f"Each person should pay: ${formatted_bill_per_person}")
