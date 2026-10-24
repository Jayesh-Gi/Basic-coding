contacts = {
    "Nikhil": 9876543212,
    "Rahuk": 1234567899,
    "Manu": 1234567894
}
name = input("Enter name:")

if name in contacts :
    print(f"{name} number:{contacts [name]}")
else:
    print("contact not found")