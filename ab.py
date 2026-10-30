# target = int(input())
# numbers = [4,7,2,9,5,8]

# for num in numbers:
#     if num == target:
#         print("Found")
#         break
#     if num % 2 == 0:
#         continue
#     print(num)


# for i in range(1,11):
#     if i % 2==0:
#         continue
#     if i == 9:
#         break
#     print(i) 

# numbers = [3, 7, 12, 5, 15, 8]

# for i in numbers:
#     if i < 10:
#         continue
#     print(i)
#     break

# numbers = [12, 7, 18, 25, 30, 9]
# for i in numbers:
#     if i % 5 != 0:
#         continue
#     if i % 5==0:
#         print(i)
#         break


# numbers = [12, 7, 20, 5, 15,4]
# total = 0
# count = 0

# for i in numbers:
#     if i % 2==0:
#         total = total + i
#         count = count + 1

# print("Sum:", total)
# print("Count:",count)

# numbers = [-12, 45, 8, -5, 67, 23, 2]
# largest = numbers[0]
# smallest = numbers[0]

# for i in numbers:
#     if i > largest:
#         largest = i
#     if i < smallest:
#         smallest = i
# print("Largets;", largest)
# print("Smallest:", smallest)

numbers = [-10, -5, -20, -2]
total = 0
count = 0
average = 0
largest = numbers[0]
smallest = numbers[0]

for i in numbers:
    total = total + i
    count = count + 1

    if count > 0:
        average = total / count
        print(average)
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i

print("Sum:", total)
print("Count:", count)
print("Average:", average)
print("Largest:",largest)
print("Smallest:",smallest)

 