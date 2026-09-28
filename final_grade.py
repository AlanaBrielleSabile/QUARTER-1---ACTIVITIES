"""
Name: Alana Brielle D. Sabile
Grade/Section: Grade 8 - Ilang-Ilang
Date Created: September 28, 2026
Program Description: This program calculates a student's final grade
using Formative Assessments, Long Test, Practical Test, and
Initial Project Proposal.
"""
import math

# Displays the program title
def display_title():
    print("==========================================")
    print("       FINAL GRADE CALCULATOR")
    print("==========================================")

# Gets and checks if a score is valid
def get_score(assessment, maximum):
    while True:
        try:
            score = int(input("Enter " + assessment + " score: "))

            if score >= 0 and score <= maximum:
                return score
            else:
                print("Invalid score. Enter a score from 0 to", maximum)

        except ValueError:
            print("Invalid input. Please enter a whole number.")

# Calculates all percentages and the final weighted grade
def calculate_grade(fa1, fa2, fa3, fa4, fa5,
                    long_test, practical_test, proposal):

    fa_total = fa1 + fa2 + fa3 + fa4 + fa5
    fa_maximum = 30 + 30 + 25 + 30 + 20

    fa_percentage = (fa_total / fa_maximum) * 100
    long_percentage = (long_test / 50) * 100
    practical_percentage = (practical_test / 60) * 100
    proposal_percentage = (proposal / 100) * 100

    # Apply the required weights
    final_grade = (
        (fa_percentage * 0.30)
        + (long_percentage * 0.30)
        + (practical_percentage * 0.30)
        + (proposal_percentage * 0.10)
    )
    # Round the final grade to two decimal places
    final_grade = math.floor(final_grade * 100 + 0.5) / 100

    return (fa_percentage, long_percentage,
            practical_percentage, proposal_percentage,
            final_grade)

# Determines the adjectival rating based on the PSHS grading scale
def get_rating(final_grade):
    if final_grade >= 96:
        return "Excellent"
    elif final_grade >= 90:
        return "Very Good"
    elif final_grade >= 78:
        return "Good"
    elif final_grade >= 66:
        return "Satisfactory"
    elif final_grade >= 55:
        return "Fair"
    elif final_grade >= 40:
        return "Failed on Condition"
    else:
        return "Failed"

# Displays the final report
def display_result(name, student_id,
                   fa1, fa2, fa3, fa4, fa5,
                   long_test, practical_test, proposal,
                   fa_percentage, long_percentage,
                   practical_percentage, proposal_percentage,
                   final_grade, rating):

    print("\n==========================================")
    print("           FINAL GRADE REPORT")
    print("==========================================")

    print("Student Name:", name)
    print("Student ID:", student_id)

    print("\nASSESSMENT SCORES")
    print("------------------------------------------")
    print("FA 1:", fa1, "/ 30")
    print("FA 2:", fa2, "/ 30")
    print("FA 3:", fa3, "/ 25")
    print("FA 4:", fa4, "/ 30")
    print("FA 5:", fa5, "/ 20")
    print("Long Test 1:", long_test, "/ 50")
    print("Practical Test:", practical_test, "/ 60")
    print("Initial Project Proposal:", proposal, "/ 100")

    print("\nCOMPONENT PERCENTAGES")
    print("------------------------------------------")
    print("Formative Assessments:", round(fa_percentage, 2), "%")
    print("Long Test:", round(long_percentage, 2), "%")
    print("Practical Test:", round(practical_percentage, 2), "%")
    print("Initial Project Proposal:", round(proposal_percentage, 2), "%")

    print("\nFINAL RESULT")
    print("------------------------------------------")
    print("Final Weighted Grade:", final_grade)
    print("Adjectival Rating:", rating)

    print("==========================================")


# Display the program title
display_title()


# Get and validate the student's name
while True:
    name = input("Enter student name: ").strip()

    if name != "":
        break
    else:
        print("Invalid input. Name cannot be blank.")


# Get and validate the student's ID
while True:
    student_id = input("Enter student ID (G8-####): ").strip().upper()

    if (student_id.startswith("G8-")
            and len(student_id) == 7
            and student_id[3:].isdigit()):
        break
    else:
        print("Invalid ID. Please use the format G8-####.")


print("\nEnter your assessment scores.")

# Get all assessment scores
fa1 = get_score("FA 1", 30)
fa2 = get_score("FA 2", 30)
fa3 = get_score("FA 3", 25)
fa4 = get_score("FA 4", 30)
fa5 = get_score("FA 5", 20)

long_test = get_score("Long Test 1", 50)
practical_test = get_score("Practical Test", 60)
proposal = get_score("Initial Project Proposal", 100)


# Calculate the grades
(fa_percentage, long_percentage,
 practical_percentage, proposal_percentage,
 final_grade) = calculate_grade(
    fa1, fa2, fa3, fa4, fa5,
    long_test, practical_test, proposal
)


# Determine the rating
rating = get_rating(final_grade)


# Display the final report
display_result(
    name, student_id,
    fa1, fa2, fa3, fa4, fa5,
    long_test, practical_test, proposal,
    fa_percentage, long_percentage,
    practical_percentage, proposal_percentage,
    final_grade, rating
)

# Reference: Philippine Science High School Student Handbook, 2017 Edition
# Academic Grades - Percent System and Adjectival Equivalent
