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

numbers = [3, 7, 12, 5, 15, 8]

for i in numbers:
    if i < 10:
        continue
    print(i)
    break
    