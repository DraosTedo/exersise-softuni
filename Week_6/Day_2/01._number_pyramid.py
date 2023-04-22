n = int(input())
current = 1
is_larger_than_n = False

for row in range(1, n + 1):
    for cow in range(1, row + 1):

        if current > n:
            is_larger_than_n = True
            break
        print(str(current) + " ", end="")
        current += 1
    if is_larger_than_n:
        break
    print()