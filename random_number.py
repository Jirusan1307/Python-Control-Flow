import random
secret = random.randint(0,10)
while True:
    guess = int(input("ทายเลข (1-10): "))
    if guess == secret:
        print("ถูกต้อง!")
        break
    elif guess < secret:
        print("น้อยไป")
    else:
        print("มากไป")
