import random #random is a built-in module is use to pick randomly.
       
score = 0 #In every code starting it will be at zero. 
computer_score = 0
total=0
a =str(input('what is your name:  '))

if a not in ' ':
    print(f'{a}! welcome to game.')
    while True:    
        list_of_the_game_stone_paper_scissor=['stone','paper','scissor']
        c = random.choice(list_of_the_game_stone_paper_scissor) #it the random.choice who will choose the string.
        print('i have choosed')  #computer choice.
        d = input('Itis your turn to chose. What you have choosed: ') #for input what you choosed.
        if d=='exit':
              #it will break when type exit and imparts accuracy.
              if total == 0:
                    print('NO GAME PLAYED.')
              else:
                    print('--------:THE ACCURACY:-------')
                    print (f'the score is {score}')
                    print(f'{a}! accuracy is {score/total*100}.')
                    print (f'the score of computer is {computer_score}')
                    print (f'Computer accuracy {computer_score/total*100}.')
                    if score>computer_score :
                         print(f'RESULT- {a} you are the winner.')
                    if computer_score > score:
                         print('RESULT- Computer is the winner.')                                    
              print ('thanks for playing it')
              break #it is for stop and break the continuously path
                    
        if  d == ' ' or d not in ['stone', 'paper', 'scissor']:
          #it is having the list of the game.
          #it is for the person if some one doesn't give any input or given wrong input according to list.
            print('ERROR')
            print ('RUN AGAIN.')
            break 
        else:
            if c =='stone' and d=='paper':
            #it will say you win the game.
                print('YOU WIN🏆.')
                score+=1
                total+=1#it will add up the score how much you win.
             
            elif c =='paper' and d=='scissor':
            #it will say you win the game.
                print('YOU WIN🏆.')
                score+=1
                total+=1#it will add up the score how much you win.
            elif c =='scissor'and d=='stone':
            #it will say you win the game.
                print('YOU WIN🏆.')
                total+=1
                score+=1
                #it will add up the score how much you win.
            elif d==c:
                total+=1
                print ('DRAW.')
            else:
            #it will say you lose the game.
                print('YOU LOSE.')  
                computer_score+=1
                print (f'Computer choice {c}')
else:
    print('ENTER YOUR NAME FIRST FROM NEXT TIME.')