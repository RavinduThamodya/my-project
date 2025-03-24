def main():
    num_courses = int(input("Enter number of courses: "))
    grades = []
    credits = []

<<<<<<< HEAD  # (Feature-WeightedGPA version)
    for i in range(num_courses):
        grade = float(input(f"Enter grade for course {i+1} (0.0 - 4.0): "))
        credit = float(input(f"Enter credits for course {i+1}: "))
        grades.append(grade)
        credits.append(credit)
=======
    for i in range(num_courses):  # (Feature-InputValidation version)
        while True:
            try:
                grade = float(input(f"Enter grade for course {i+1} (0.0 - 4.0): "))
                if 0.0 <= grade <= 4.0:
                    grades.append(grade)
                    break
                else:
                    print("Invalid input! Please enter a grade between 0.0 and 4.0.")
            except ValueError:
                print("Invalid input! Please enter a numeric grade.")
>>>>>>> Feature-InputValidation
