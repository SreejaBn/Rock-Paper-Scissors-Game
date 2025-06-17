import random

l = ['rock', 'paper', 'scissor']

print ('This a rock paper scissor game.')
print ("\nTo clear any doubts, as a computer, i don't have a mind of my own and i can't cheat. so even if u type your answer first, i won't change my choice. so, rest assured.")
print ('Here are the rules: if u won, u get +1, if i won, u get -1 and if it is a draw, u get 0 points. The total number of rounds is 5 in a single game.')
while True:
    points = 0
    
    for i in range(5):
            
        while True:
            user = input ('What is your choice?\n').lower().strip().rstrip('s')
            if user not in l:
                print ('Invalid input. This round is not counted. Try again.')
            else:
                break
        choice = random.choice(l)
        print (f'My choice is {choice}') 

        if choice == user:
            print ('its a draw. -_-')
        elif (choice == 'rock' and user == 'paper') or (choice == 'paper' and user == 'scissor') or (choice == 'scissor' and user == 'rock'):
            print ('Wow! u got that one.')
            points += 1
        else:
            print ('I won!!! >-<')
            points -= 1

    print ('Your score is:', points, 'out of 5 points.')

    while True:
        f= input ("Do u want to play again? Type y for yes and n for no.").lower().strip()
        if f == 'n':
            print ("It was fun playing with u.")
            exit()
        elif f == 'y':
            print ("up we go for another round!!")
            break
        else:
            print ('Invalid input. Type again.')