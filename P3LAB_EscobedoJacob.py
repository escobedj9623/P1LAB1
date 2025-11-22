# ---------------------------------------------------------
# Name: Jacob Escobedo
# Program: P3LAB
# Description:
# This program takes a money value from the user and
# calculates the most efficient number of dollars,
# quarters, dimes, nickels, and pennies needed.
# ---------------------------------------------------------

# Ask user for amount
amount = float(input("Enter amount of money: "))

# Convert amount to integer cents
cents = int(amount * 100)

# Dollar calculations
dollars = cents // 100
cents -= dollars * 100

quarters = cents // 25
cents -= quarters * 25

dimes = cents // 10
cents -= dimes * 10

nickels = cents // 5
cents -= nickels * 5

pennies = cents

# Display results
# Only print when quantity > 0 and handle singular/plural

if dollars > 0:
    if dollars == 1:
        print("1 dollar")
    else:
        print(f"{dollars} dollars")

if quarters > 0:
    if quarters == 1:
        print("1 quarter")
    else:
        print(f"{quarters} quarters")

if dimes > 0:
    if dimes == 1:
        print("1 dime")
    else:
        print(f"{dimes} dimes")

if nickels > 0:
    if nickels == 1:
        print("1 nickel")
    else:
        print(f"{nickels} nickels")

if pennies > 0:
    if pennies == 1:
        print("1 penny")
    else:
        print(f"{pennies} pennies")
