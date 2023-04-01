student_name = input()
grade_counter = 0
year_counter = 0
failed_years = 0

while True:
    annual_grade = float(input())

    if annual_grade < 4:
        failed_years += 1

        if failed_years == 2:
            current_failed_years = failed_years + 1
            print(f"{student_name} has been excluded at {current_failed_years} grade")
            break
        continue

    year_counter += 1
    grade_counter += annual_grade

    if year_counter == 12:
        average_grade = grade_counter / 12
        print(f"{student_name} graduated. Average grade: {average_grade}")