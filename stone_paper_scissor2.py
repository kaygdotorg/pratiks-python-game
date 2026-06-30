import random  # built-in module, used here to let the computer pick randomly

# Scores start at zero at the beginning of every run.
score = 0           # how many rounds YOU win
computer_score = 0  # how many rounds the COMPUTER wins
total = 0           # total rounds actually played (win + lose + draw)

name = input('What is your name: ')

# BUG FIX 1: original was "if a not in ' '", which checks if the name is a
# substring of a single space. That is not what we want. We just want to make
# sure the player typed an actual name and not blank/spaces. .strip() removes
# surrounding spaces, so an empty or spaces-only name fails this check.
if name.strip() != '':
    print(f'{name}! Welcome to the game.')

    while True:
        choices = ['stone', 'paper', 'scissor']
        computer = random.choice(choices)  # the computer's random pick

        you = input('Your turn. Type stone, paper, scissor, or exit: ').lower()
        # .lower() means "Stone", "STONE" and "stone" all work the same.

        if you == 'exit':
            # Show the summary when the player chooses to quit.
            if total == 0:
                print('NO GAME PLAYED.')
            else:
                print('--------: THE ACCURACY :--------')
                print(f'Your score is {score}')
                print(f'{name}! Your accuracy is {score / total * 100:.1f}%.')
                print(f'Computer score is {computer_score}')
                print(f'Computer accuracy is {computer_score / total * 100:.1f}%.')

                if score > computer_score:
                    print(f'RESULT- {name}, you are the winner.')
                elif computer_score > score:
                    print('RESULT- Computer is the winner.')
                else:
                    print('RESULT- It is a tie.')

            print('Thanks for playing.')
            break  # leaves the while loop and ends the program

        # BUG FIX 2: original used "break" here, which ended the whole game on a
        # single typo. We use "continue" so a bad input just asks again.
        if you not in choices:
            print('ERROR: please type stone, paper, scissor, or exit.')
            continue  # jump back to the top of the loop, do NOT count this round

        # Show what the computer chose so the result makes sense to the player.
        print(f'Computer chose {computer}.')

        # From here a real round was played, so every outcome below counts.
        if you == computer:
            print('DRAW.')
            total += 1
        elif (you == 'paper' and computer == 'stone') or \
             (you == 'scissor' and computer == 'paper') or \
             (you == 'stone' and computer == 'scissor'):
            print('YOU WIN.')
            score += 1
            total += 1
        else:
            # BUG FIX 3: original forgot "total += 1" here, so losses were never
            # counted. That made the accuracy math wrong. Now losses count too.
            print('YOU LOSE.')
            computer_score += 1
            total += 1
else:
    print('ENTER YOUR NAME FIRST NEXT TIME.')
