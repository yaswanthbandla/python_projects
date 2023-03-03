import random

def play():

        user=(input(" sleect one 'r' for rock, 'p' for paper, 's' for sicssor : "))
        computer=random.choice(['r','p','s'])

        if user==computer:
            return "it's a tie"
        if user_win(user,computer):
            return " hurray!!! I won "
        return "it's okay, I lost"


def user_win(p1,p2):
    if p1=='s' and p2=='p' or p1=='p' and p2=='r' or p1=='r' and p2=='s':
        return True
def main():
    t=int(input())
    while t>0:
        print(play())
        t=t-1
main()