target = int(input())
numbers = [4,7,2,9,5,8]

for num in numbers:
    if num == target:
        print("Found")
        break
    if num % 2 == 0:
        continue
    print(num)


for i in range(1,11):
    if i % 2==0:
        continue
    if i == 9:
        break
    print(i) 

numbers = [3, 7, 12, 5, 15, 8]

for i in numbers:
    if i < 10:
        continue
    print(i)
    break

numbers = [12, 7, 18, 25, 30, 9]
for i in numbers:
    if i % 5 != 0:
        continue
    if i % 5==0:
        print(i)
        break


numbers = [12, 7, 20, 5, 15,4]
total = 0
count = 0

for i in numbers:
    if i % 2==0:
        total = total + i
        count = count + 1

print("Sum:", total)
print("Count:",count)

numbers = [-12, 45, 8, -5, 67, 23, 2]
largest = numbers[0]
smallest = numbers[0]

for i in numbers:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i
print("Largets;", largest)
print("Smallest:", smallest)

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


sales = {
    "apple": 30,
    "banana": 20,
    "mango": 50,
    "orange": 40
}
total = 0
for price in sales.values():
    total = total + price

print("Total Sales:",total)

products = {
    "laptop": 50000,
    "mouse": 500,
    "keyboard": 1500,
    "monitor": 12000
}
max_price = 0
best_product = ""

for product,price in products.items():
    if price > max_price:
        max_price = price
        best_product = product
print("Most Expensive:", best_product)
print("Price:",max_price)


products = {
    "laptop": 50000,
    "mouse": 500,
    "keyboard": 1500,
    "monitor": 12000,
    "phone": 30000
}
expensive = 0

for product,price in products.items():
    if price > 10000:
        expensive +=1
print("Expensive Products:",expensive)

word = "programming"
counts = {}

for char in word:
    counts[char] = counts.get(char, 0) + 1
print(counts)

students = {
    "Aman": 85,
    "Riya": 45,
    "Karan": 67,
    "Simran": 95,
    "Rahul": 32,
    "Priya": 78
}
total = 0
student_passed = 0
student_failed = 0
top_students = []

for student, marks in students.items():
    total +=marks
    if marks >= 40:
        student_passed += 1
    else:
        student_failed += 1
    if marks > 75:
        top_students.append(student)
        
average=total/len(students)

print("Total Marks:", total)
print("Average Marks:", average)
print("Passed:", student_passed)
print("Failed:", student_failed)
print("Students Above 75:", ", ".join(top_students))

employees = {
    "Aman": 35000,
    "Riya": 50000,
    "Karan": 28000,
    "Simran": 65000,
    "Rahul": 42000
}
total = 0
highest_salary = 0
top_employee = ""

for employee, salary in employees.items():
    if salary > highest_salary:
        highest_salary = salary
        top_employee = employee