n = int(input())
i = 0

while i < n:
    i += 1

    if i == 5:
        continue
    elif i == 8:
        break
    else:
        print(i)