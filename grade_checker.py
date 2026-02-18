# Grade Calculator Program

# Ask user for their test score
score = float(input("Enter your test score (0-100): "))

# Validate input
if score < 0 or score > 100:
    print("Invalid score! Please enter a score between 0 and 100.")
else:
    # Determine letter grade using if-else statements
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    
    # Print the result with a message
    print(f"Your score: {score}")
    print(f"Your grade: {grade}")
    
    # Additional feedback based on grade
    if grade == "A":
        print("Excellent work! Keep it up!")
    elif grade == "B":
        print("Great job! You're doing well.")
    elif grade == "C":
        print("Good effort! You passed.")
    elif grade == "D":
        print("You passed, but there's room for improvement.")
    else:
        print("You need to study more for the next test.")
