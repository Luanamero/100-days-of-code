#Tip calculator

print("Welcome to the tip calculator!")

first_price = float(input("What was the total bill? $"))

tip = int(input("What percentage tip would you like to give? 10, 12 or 15?"))

people = int(input("How many people to split the bill?"))

total = first_price + (first_price * tip) / 100
individual = (total / int(people))
final_result = "{:.2f}".format(individual)
print(f"Each person should pay: ${final_result}")
