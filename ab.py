secret_number= 7
guess =0

while guess!= secret_number:
    guess = int(input("Guess the number (1 to 10):"))

    if guess < secret_number:
        print("Too short! Think some bigger ")
    elif guess > secret_number:
        print("Too big! Think little small")
    else:
        print("Congratulation you gessed the number")
