saving_amount = float(input())
monthly_amount = float(input())
months = int(input())


for i in range(1 ,months+1):
    saving_amount +=monthly_amount
    print(f"Month {i}: {saving_amount:.2f}")




Total_deposited = monthly_amount * months

print(f"balance {saving_amount:.2f}")
print(f"Total deposited: {Total_deposited :.2f}")