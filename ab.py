marks = input().split(",")
total = 0
passed = 0
failed = 0
highest = 0

for mark in marks:
    mark = int(mark)
    total += mark

    if mark >= 40:
        passed +=1
    else:
        failed +=1
    if mark > highest:
        highest = mark

print("Total marks:", total)
print("Passed subjects: ", passed)
print("Failed subjects:", failed)
print("Highest marks:", highest)