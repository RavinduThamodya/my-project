def calculate_gpa(grades):
    if not grades:
        return 0.0
    return sum(grades) / len(grades)

def main():
    num_courses = int(input("Enter number of courses: "))
    grades = []

    for i in range(num_courses):
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

    gpa = calculate_gpa(grades)
    print(f"Your Semester GPA is: {gpa:.2f}")

if __name__ == "__main__":
    main()
