def calculate_weighted_gpa(grades, credits):
    total_weighted_score = sum(grade * credit for grade, credit in zip(grades, credits))
    total_credits = sum(credits)
    return total_weighted_score / total_credits if total_credits > 0 else 0.0

def main():
    num_courses = int(input("Enter number of courses: "))
    grades = []
    credits = []

    for i in range(num_courses):
        while True:
            try:
                grade = float(input(f"Enter grade for course {i+1} (0.0 - 4.0): "))
                credit = float(input(f"Enter credits for course {i+1}: "))
                if 0.0 <= grade <= 4.0 and credit > 0:
                    grades.append(grade)
                    credits.append(credit)
                    break
                else:
                    print("Invalid input! Ensure grade is between 0.0 - 4.0 and credits are positive.")
            except ValueError:
                print("Invalid input! Please enter numeric values.")

    gpa = calculate_weighted_gpa(grades, credits)
    print(f"Your Weighted Semester GPA is: {gpa:.2f}")

if __name__ == "__main__":
    main()
