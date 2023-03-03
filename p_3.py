import random
def find_a_number(x):
    my_number=int(input())
    guess=0
    c=0
    while guess!=my_number:
        guess=random.randint(1,x)
        c+=1
        if guess<my_number:
            print(f"{guess} is t00 low.....")
        elif guess>my_number:
            print(f"{guess} is too high....")
    print(f"Yay...the computer guessed your {guess} correctly... but it takes {c} times")
find_a_number(50)