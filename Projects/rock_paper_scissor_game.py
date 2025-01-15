'''
Soecifically for python beginners
Author: Arta Khosravi
Last edit: Jan. 2025
'''
#  #ex 1: computer always winning scenario
# from random import randint
# class RPS:
#     def RPS(self):
#         inp = input('Enter (rock/paper/scissor): ')
#         inputs = {'rock':'paper','paper':'scissor','scissor':'rock'}    
#         if inp.lower() in inputs:
#             ans = inputs[inp]
#             print ('Take that! {}!'.format(ans))
#             return ans
#         else:
#             print('Error: Retype.')
# ans = RPS()
# ans.RPS()

#ex 2: sets of game included:
from random import randint
play = True
while play:
    num_sets = input('How many sets do you want to play? ')
    try: #using try and except in a while loop when
        #you want the loop to understand that an action
        #will 100% happen, unless an for example error occurs.
        num_sets = int(num_sets)
        player_score = 0
        computer_score = 0
        for i in range(num_sets): #using this for loop because i want it to loop exactly in the number of the num_sets.
            inp = input('Enter (rock/paper/scissor): ')
            inputs = ['rock', 'paper', 'scissor']
            ramdom_n = randint(0, 2)
            ans = inputs[ramdom_n]
            beat_inputs = {'rock':'paper','paper':'scissor','scissor':'rock'}    

            if inp.lower() in inputs:
                print('Computers choice is: {}.'.format(ans.upper()))
                if inp.lower() == ans:
                    print("It's a tie!")
                elif ans == beat_inputs[inp]:
                    print("You win this round!")
                    player_score += 1
                else:
                    print("You lose this round!")
                    computer_score += 1
            else:
                print('Error: Retype.')

        if computer_score < player_score:
            print('You win with {} vs. {}!'.format(player_score,computer_score))
        elif computer_score > player_score:
            print('Computer wins with {} vs. {}!'.format(computer_score,player_score))
        else:
            print('The game is a tie with {}!'.format(player_score))
        
        play_again = input('Do you want to play again? (y/n): ')
        if play_again.lower() == 'n':
            break
    except ValueError:
        p_a = input('Invalid. Want to try again? (y/n) ')
        if p_a.lower() == 'n':
            break
