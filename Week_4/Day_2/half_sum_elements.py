import sys

n = int(input())
sum_number = 0
max_num = -sys.maxsize

for i in range(n):
    current_number = int(input())
    sum_number += current_number
    if current_number > max_num:
        max_num = current_number

sum_number -= max_num

if max_num == sum_number:
    print("Yes")
    print(f"Sum = {sum_number}")
else:
    print("No")
    print(f"Diff = {abs(sum_number - max_num)}")
    
