# Jacob Escobedo
# November 7, 2025
# P1HW2 - Travel Budget Program
# This program asks the user for their trip budget and expenses (gas, accommodation, and food),
# calculates total expenses, and displays the remaining balance.

# Pseudocode:
# 1. Ask user to enter budget
# 2. Ask user to enter travel destination
# 3. Ask user to enter gas expense
# 4. Ask user to enter accommodation expense
# 5. Ask user to enter food expense
# 6. Add all expenses together
# 7. Subtract total expenses from budget to get remaining balance
# 8. Display the travel destination, total expenses, and remaining balance

# Get user input
budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas = float(input("How much do you think you will spend on gas? "))
accommodation = float(input("Approximately, how much will you need for accommodation/hotel? "))
food = float(input("Last, how much do you need for food? "))

# Calculate total expenses and remaining balance
total_expenses = gas + accommodation + food
remaining_balance = budget - total_expenses

# Display results
print()
print("------------Travel Expenses------------")
print("Location:", destination)
print("Initial Budget:", budget)
print()
print("Fuel:", gas)
print("Accommodation:", accommodation)
print("Food:", food)
print("---------------------------------------")
print("Remaining Balance:", remaining_balance)
