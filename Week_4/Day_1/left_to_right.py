n = int(input())

left_sum = 0
right_sum = 0

for number in range (0, n*2):
    current_number = int(input())

    if number < n:
        left_sum += current_number
    elif number >= n:
        right_sum += current_number


if left_sum == right_sum:
    print(f"Yes, sum = {right_sum}")
else:
    diff = abs(left_sum - right_sum)
    print(f"No, diff = {diff}")
