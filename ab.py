text = input()
vowels = "aeiou"
count = 0

for ch in text:
    if ch.lower() not in vowels:
        continue
    count +=1

    if count == 3:
        break
print("Vowels:", count)

