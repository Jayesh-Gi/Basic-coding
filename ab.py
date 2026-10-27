item1 = input()
qty1 = int(input())

item2 = input()
qty2 = int(input())

updated_item = input()
extra = int(input())

borrowing = {
    item1:qty1,
    item2:qty2
}

borrowing[updated_item] +=extra

updated_qty = borrowing[updated_item]

if updated_qty >= 25:
    level= "Busy"
elif updated_qty >= 12:
    level = "Moderate"
else:
    level = "Quiet"

total = sum(borrowing.values())

if borrowing[item1] > borrowing[item2]:
    highest_item = item1

else:
    highest_item = item2

highest_qty = borrowing[highest_item]

print("Highest:" , highest_item, "-", highest_qty) 
print("Borrowing:")
