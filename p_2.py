import random
def find_rand_num(x):
    rand_num=random.randint(1,x)
    guess=0
    while guess!=rand_num:
        guess=int(input())
        if guess<rand_num:
            print("too low.....")
        elif guess>rand_num:
            print("too high....")
    print("Hurray!!!!!!!.....you guessed it correct")
find_rand_num(50)