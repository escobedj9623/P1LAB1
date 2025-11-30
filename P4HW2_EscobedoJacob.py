# Jacob Escobedo
# 11/29/2025
# P4HW2 – Salary Calculator
# This program calculates regular pay, overtime pay, and gross pay
# for multiple employees using a sentinel loop. At the end it displays
# total overtime paid, total regular pay, total gross pay, and number
# of employees processed.

"""
PSEUDOCODE:

1. Initialize totals:
       total_overtime_pay = 0
       total_regular_pay = 0
       total_gross_pay = 0
       employee_count = 0

2. Ask user for employee name
       input employee_name

3. While employee_name is NOT "Done":
       a. Ask for hours worked
       b. Ask for pay rate

       c. If hours > 40:
              overtime_hours = hours - 40
              overtime_pay = overtime_hours * (rate * 1.5)
              regular_pay = 40 * rate
         Else:
              overtime_hours = 0
              overtime_pay = 0
              regular_pay = hours * rate

       d. gross_pay = regular_pay + overtime_pay

       e. Add to totals:
              total_regular_pay += regular_pay
              total_overtime_pay += overtime_pay
              total_gross_pay += gross_pay
              employee_count += 1

       f. Display employee summary

       g. Ask for next employee name

4. After loop ends (user enters "Done"):
       Display:
           Number of employees
           Total overtime pay
           Total regular pay
           Total gross pay
"""

# ---------------- PROGRAM START ----------------

total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0
employee_count = 0

employee_name = input("Enter employee's name or 'Done' to terminate: ")

while employee_name != "Done":

    hours = float(input(f"Enter hours worked by {employee_name}: "))
    rate = float(input(f"Enter {employee_name}'s pay rate: "))

    if hours > 40:
        overtime_hours = hours - 40
        overtime_pay = overtime_hours * (rate * 1.5)
        regular_pay = 40 * rate
    else:
        overtime_hours = 0
        overtime_pay = 0
        regular_pay = hours * rate

    gross_pay = regular_pay + overtime_pay

    # Update totals
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay
    employee_count += 1

    # Display employee pay breakdown
    print("----------------------------------------")
    print(f"Employee name: {employee_name}")
    print(f"Overtime pay: ${overtime_pay:,.2f}")
    print(f"Regular pay:  ${regular_pay:,.2f}")
    print(f"Gross pay:    ${gross_pay:,.2f}")
    print("----------------------------------------\n")

    employee_name = input("Enter another employee's name or 'Done' to terminate: ")

print("\n========== PAY SUMMARY ==========")
print(f"Total number of employees: {employee_count}")
print(f"Total overtime pay:        ${total_overtime_pay:,.2f}")
print(f"Total regular pay:         ${total_regular_pay:,.2f}")
print(f"Total gross pay:           ${total_gross_pay:,.2f}")
print("=================================")
