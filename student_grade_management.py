

# Student Grade Management System

courses = [
    "Inclusiveness",
    "Software Process Improvement",
    "Continuous Integration and Deployment",
    "Service Oriented Architecture",
    "Systems Thinking and Systems Approach",
    "Knowledge Discovery and Data Mining"
]

# Each course has 3 credit hours
credit_hours = [3, 3, 3, 3, 3, 3]


def calculate_grade(mark):
    """Return the letter grade and grade points."""

    if 95 <= mark <= 100:
        return "A+", 4.00
    elif 85 <= mark < 95:
        return "A", 4.00
    elif 80 <= mark < 85:
        return "A-", 3.70
    elif 75 <= mark < 80:
        return "B+", 3.50
    elif 65 <= mark < 75:
        return "B", 3.00
    elif 60 <= mark < 65:
        return "B-", 2.70
    elif 55 <= mark < 60:
        return "C+", 2.50
    elif 50 <= mark < 55:
        return "C", 2.00
    elif 45 <= mark < 50:
        return "C-", 1.75
    elif 40 <= mark < 45:
        return "D", 1.00
    else:
        return "F", 0.00


def get_valid_mark(course):
    """Accept only numeric marks between 0 and 100."""

    while True:
        try:
            mark = float(input(f"Enter mark for {course} (0-100): "))

            if 0 <= mark <= 100:
                return mark

            print("Invalid mark! Enter a value from 0 to 100.")

        except ValueError:
            print("Invalid input! Please enter a number.")


def main():
    print("=" * 65)
    print("           STUDENT GRADE MANAGEMENT SYSTEM")
    print("=" * 65)

    # Get student information
    while True:
        name = input("Enter student name: ").strip()

        if name:
            break

        print("Student name cannot be empty.")

    # Collect marks and calculate grades
    results = []

    for course in courses:
        mark = get_valid_mark(course)
        letter, points = calculate_grade(mark)
        results.append((course, mark, letter, points))

    # Calculate total and average marks
    total_marks = sum(result[1] for result in results)
    average_mark = total_marks / len(courses)

    # Calculate total credit hours
    total_credits = sum(credit_hours)

    # Calculate weighted GPA
    weighted_points = sum(
        results[i][3] * credit_hours[i]
        for i in range(len(courses))
    )

    gpa = weighted_points / total_credits

    # Calculate overall letter grade from average mark
    overall_grade, _ = calculate_grade(average_mark)

    # Display results
    print("\n" + "=" * 85)
    print("                         STUDENT RESULTS")
    print("=" * 85)
    print(f"Student Name: {name}")
    print("-" * 85)

    print(
        f"{'Course':43} {'Mark':>7} {'Grade':>7} "
        f"{'Points':>8} {'Credits':>8}"
    )
    print("-" * 85)

    for i, (course, mark, letter, points) in enumerate(results):
        print(
            f"{course[:43]:43} {mark:7.2f} {letter:>7} "
            f"{points:8.2f} {credit_hours[i]:8}"
        )

    print("-" * 85)
    print(f"Total Marks: {total_marks:.2f} / {len(courses) * 100}")
    print(f"Average Mark: {average_mark:.2f}%")
    print(f"Overall Letter Grade: {overall_grade}")
    print(f"Total Credit Hours: {total_credits}")
    print(f"Semester GPA: {gpa:.2f} / 4.00")
    print("=" * 85)


if __name__ == "__main__":
    main()
