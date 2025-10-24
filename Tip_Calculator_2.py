print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_percent=tip/100
multiplier=1+tip_percent

pay=(bill/people)*multiplier

print(f"Please pay {pay} per person")
