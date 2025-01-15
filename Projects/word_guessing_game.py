'''
Soecifically for python beginners
Author: Arta Khosravi
Last edit: Jan. 2025
'''
import sys
import random
word_list = ["apple", "book", "desk", "pen", "cat", "dog", "tree", "house", "car", "phone",
             "computer", "laptop", "keyboard", "mouse", "chair", "table", "door", "window", "wall", "floor"]
word = str(random.choice(word_list))
turn = int(input('How many turns do you want to have? ')) #how many turns player has
guess = '' #players guess will be saved here (initially null)
hint = input ('Do you want a hint on how many characters this word has? (y/n) ')
if hint.lower() == 'y':
    print('This word has {} characters.'.format(len(word)))
while turn > 0: #as long as the player has a guess
    print()
    inp = input('Enter a character: ')
    if len(inp) != 1: #if the player entered more than 1 characters, warn and restart the loop
        print('Please enter only one (1) character.')
        continue
    if inp in guess:
        print('You have already guessed "{}"!'.format(inp))
        continue
    guess += inp #add the character to player's guess (in a loop)
    if inp not in word: #if the character wasn't in the considered word
        turn -= 1 #remove one of player's turns
        print('Wrong answer! You have {} turns.'.format(turn))
        if turn == 0:
            print('The word was ' + word)
        continue
    win = True
    for c in word:
        if c in guess: #if a character in the initial word was guessed correctly by the player,
            sys.stdout.write(c) #then print it
        else:
            sys.stdout.write('_') #otherwise print _ without inlines, all in a line
            win = False
    if win:
        print()
        print('Congratulations! You have won!')
        break
if not win:
    print()
    print('You have lost :(')
print('Your turn is finished.')
