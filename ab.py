target = int(input())
numbers = [4,7,2,9,5,8]

for num in numbers:
    if num == target:
        print("Found")
        break
    if num % 2 == 0:
        continue
    print(num)