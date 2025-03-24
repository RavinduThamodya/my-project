def calculate_gpa(grades):
    """Calculate GPA from a list of grades (0.0 - 4.0 scale)."""
    if not grades:
        return 0.0
    return sum(grades) / len(grades)

def main():
    num_courses = int(input("Enter number of courses: "))
    grades = []

    for i in range(num_courses):
        grade = float(input(f"Enter grade for course {i+1} (0.0 - 4.0): "))
        grades.append(grade)

    gpa = calculate_gpa(grades)
    print(f"Your Semester GPA is: {gpa:.2f}")

if __name__ == "__main__":
    main()
