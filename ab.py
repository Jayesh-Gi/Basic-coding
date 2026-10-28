
password = input()

uppercase = 0
lowercase = 0
digit = 0
special = 0

for char in password:
    if char.isupper():
        uppercase += 1
    elif char.islower():
        lowercase += 1
    elif char.isdigit():
        digit += 1
    elif not char.isspace():
        special += 1

categories = 0

if uppercase > 0:
    categories += 1
if lowercase > 0:
    categories += 1
if digit > 0:
    categories += 1
if special > 0:
    categories += 1

if len(password) >= 8 and categories == 4:
    strength = "Strong"
elif len(password) >= 6 and categories >= 3:
    strength = "Medium"
else:
    strength = "Weak"

print("Uppercase:", uppercase)
print("Lowercase:", lowercase)
print("Digits:", digit)
print("Special characters:", special)
print("Password strength:", strength)
