number = int(input())

left_summ = 0
right_summ = 0


for i in range (2):
    first_num = int(input())
    second_num = int(input())
    left_summ = left_summ + first_num
    right_summ = right_summ + right_summ

    if left_summ == right_summ:
        print(f"Yes, sum = {left_summ}")

    else:
        diff = abs(left_summ - right_summ)
        print(f"No, diff = {diff}")

