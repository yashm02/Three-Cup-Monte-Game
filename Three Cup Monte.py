
from random import shuffle

#initial list
my_list=[' ','O',' ']

#shuffle list
def shuffle_list(my_list):
    shuffle(my_list)
    return my_list

mixed_list=shuffle_list(my_list)

#player guess
def player_guess():
    guess=''
    while guess not in ['0','1','2']:
        guess=input("PICK A NUMBER FROM 0, 1 or 2: ")

    return int(guess)

guess=player_guess()

# check guess
def check_guess(my_list,guess):
    if(my_list[guess]=='O'):
        print("CONGRATULATIONS, YOU ARE RIGHT!!!")
    else:
        print("OOPS, WRONG GUESS!!!")
        print("TRY AGAIN")
        print(my_list)

check_guess(mixed_list,guess)
