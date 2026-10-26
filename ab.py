item1 = input()
qty1 = int(input())

item2 = input()
qty2 = int(input())

updated_item = input()
extra =  int(input())

stock = {
    item1: qty1,
    item2: qty2
}

stock[updated_item] += extra

updated_qty = stock[updated_item]

if updated_qty >=30:
    level =  "High"
elif updated_qty >=15:
    level = "Medium"
else:
    level = "Low"

total = sum(stock.values())


if stock[item1] > stock[item2]:
    highest_item = item1
else:
    highest_item = item2

print("Stock:")
print(f"{item1}: {stock[item1]}")
print(f"{item2}: {stock[item2]}")
print(f"Updated: {updated_item} - {updated_qty}")
print(f"Level: {level}")
print(f"Total: {total}")
print(f"Highest: {highest_item} - {stock[highest_item]}")