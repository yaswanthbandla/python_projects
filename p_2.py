import random
def guess_a_number(x):
    ran_number=random.randint(1,x)
    guess=0
    while guess!=ran_number:
        guess=int(input(f"guess a number betwwen 1 and {x}: "))
        if guess<ran_number:
            print("sorry.too low")
        elif guess>ran_number:
            print("sorry, too high")
    print(f"wooah!!!!, you guessed correct it is {ran_number}")
guess_a_number(50)