# Jacob Escobedo
# Date
# P4HW1 - Score List and Grade Calculator
# This program collects a number of test scores from the user, validates each score,
# stores them in a list, removes the lowest score, calculates the average,
# and displays a letter grade based on that average.

"""
Pseudocode (Detailed Algorithm)

1. Ask user how many scores they want to enter -> store as num_scores.
2. Create an empty list called scores.

3. Loop from 1 to num_scores:
    a. Ask user to enter a score.
    b. While score is NOT between 0 and 100:
         - Display error message.
         - Ask for a VALID score.
    c. Add valid score to the scores list.

4. After loop ends:
    - Find lowest score -> store as lowest.
    - Create a new list without the lowest score -> modified_scores.
    - Calculate average of modified_scores.

5. Determine letter grade:
    If average >= 90 -> A
    Else if average >= 80 -> B
    Else if average >= 70 -> C
    Else if average >= 60 -> D
    Else -> F

6. Display:
    - Lowest score
    - Modified score list
    - Average of scores
    - Letter grade
"""

# Step 1: Ask user for number of scores
num_scores = int(input("How many scores would you like to enter? "))

# Step 2: Create list
scores = []

# Step 3: Loop to collect valid scores
for i in range(1, num_scores + 1):
    score = float(input(f"Enter score #{i}: "))

    # Validate score
    while score < 0 or score > 100:
        print("INVALID score entered! Score must be between 0 and 100.")
        score = float(input(f"Enter a VALID score #{i}: "))

    scores.append(score)

# Step 4: Process results
lowest = min(scores)
scores_modified = scores.copy()
scores_modified.remove(lowest)

average = sum(scores_modified) / len(scores_modified)

# Step 5: Determine letter grade
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

# Step 6: Display results
print("\n---------- Results ----------")
print(f"Lowest Score  : {lowest}")
print(f"Modified List : {scores_modified}")
print(f"Average Score : {average:.2f}")
print(f"Letter Grade  : {grade}")
print("-----------------------------")
