pin = int(input("Enter your pin number:"))

if pin == 1234:
    print("Correct Pin")
elif amount <= 0:
    print("Invalid Amount")
elif amount > balance:
    print("Insufficient Balance")
else:
    print("Withdrawl Successful")
    print("Remaining balance:", balance-amount)







