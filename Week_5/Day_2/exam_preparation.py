failed_treshold = int(input())
failed_count = 0
score_sum = 0
score_count = 0
last_task_name = ""
has_failed = True

while failed_count < failed_treshold:
    task_name = input()
    if task_name == "Enough":
        has_failed = False
        break

    task_grade = int(input())
    score_sum += task_grade
    score_count += 1
    last_task_name = task_name

    if task_grade <= 4:
        failed_count += 1

if has_failed:
    print(f"You need a break, {failed_count} poor grades.")
else:
    print(f"Average score: {score_sum / score_count:.2f}")
    print(f"Number of problems: {score_count}")
    print(f"Last problem: {last_task_name}")