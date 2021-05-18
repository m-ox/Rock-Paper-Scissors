'''#######################################################################################################################
#   r o c k  b e a t s  s c i s s o r s  -  p a p e r  b e a t s  r o c k  -  s c i s s o r s  b e a t s  p a p e r   #
#######################################################################################################################

                           dP                                                                              
                           88                                                                              
88d888b. .d8888b. .d8888b. 88  .dP     88d888b. .d8888b. 88d888b. .d8888b. 88d888b.                        
88'  `88 88'  `88 88'  `"" 88888"      88'  `88 88'  `88 88'  `88 88ooood8 88'  `88             god why           
88       88.  .88 88.  ... 88  `8b.    88.  .88 88.  .88 88.  .88 88.  ... 88                           :')      
dP       `88888P' `88888P' dP   `YP    88Y888P' `88888P8 88Y888P' `88888P' dP                              
                                       88                88                                                
                                       dP                dP                                                
                  oo                                                                                       
                                                                                                           
.d8888b. .d8888b. dP .d8888b. .d8888b. .d8888b. 88d888b. .d8888b.    .d8888b. .d8888b. 88d8b.d8b. .d8888b. 
Y8ooooo. 88'  `"" 88 Y8ooooo. Y8ooooo. 88'  `88 88'  `88 Y8ooooo.    88'  `88 88'  `88 88'`88'`88 88ooood8 
      88 88.  ... 88       88       88 88.  .88 88             88    88.  .88 88.  .88 88  88  88 88.  ... 
`88888P' `88888P' dP `88888P' `88888P' `88888P' dP       `88888P'    `8888P88 `88888P8 dP  dP  dP `88888P' 
                                                                          .88                              
                                                                      d8888P                               

#######################################################################################################################
#   r o c k  b e a t s  s c i s s o r s  -  p a p e r  b e a t s  r o c k  -  s c i s s o r s  b e a t s  p a p e r   #
####################################################################################################################'''

import random

## GLOBAL VARIABLES ##
game_start = True

## THE RANDOMIZER ##

def randomizer(odds_and_ends):

    results_list = list(odds_and_ends.copy().keys())
    weights_list = list(odds_and_ends.copy().values())

    random_list = random.choices(
        results_list, weights=(weights_list), k=1)

    return random_list[0]


## RANDOM DICTIONARY ##

random_phrase_dictionary = {
    'selection_weights': {
        'What move would you like to make?\n\n*************************************': 1,
        'Choose your weapon.\n\n*************************************': 1,
        'Pick your battle instrument.\n\n*************************************': 1,
        'Make a selection.\n\n*************************************': 3
    },

    'winning_weights': {
        'You did pretty good there.\n': 1,
        'That\'s called winning, son.\n': 1,
        'Honestly was kind of hoping you\d lose this time...\n': 1
    },

    'losing_weights': {
        'That sucks. I\'m sorry.\n': 10,
        'I was expecting more out of that...\n': 10,
        'Hank Hill: YOU\'RE A LOSER. A LOSER.\n': 1
    },

    'opponent_selection': {
        (0, 'rock'): 5,
        (1, 'paper'): 5,
        (2, 'scissor'): 5,
        (3, 'gun'): 1
    },
}

#print(list(random_phrase_dictionary['opponent_selection'].keys())[0][0]) #holy f*ck - can now select the 'index' of opponent weapons


## RANDOM PHRASE FOR MAKE A SELECTION ##

def make_a_selection_narration():
    result = randomizer(random_phrase_dictionary['selection_weights'])
    print(result)

#make_a_selection_narration() - FOR DEBUGGING PURPOSES


## PLAYER WEAPON SELECTION ##

def player_weapon_selection():
    while True:
        your_weapon = input('(1) ROCK - (2) PAPER - (3) SCISSORS : ').lower()
        
        if your_weapon == 'rock' or your_weapon == '1':
          your_weapon = 0
          print('\nYou have selected the humble rock...\n')
          return your_weapon

        elif your_weapon == 'paper' or your_weapon == '2':
          your_weapon = 1
          print('\nYou have selected the esteemed paper.\n')
          return your_weapon

        elif your_weapon == 'scissors' or your_weapon == '3':
          your_weapon = 2
          print('\nYou have selected the cunning scissors.\n')
          return your_weapon

        elif your_weapon == 'gun':
          your_weapon = 3
          print('\nYou have selected gun for some reason...\nPretty sure that\'s cheating, but whatever.\n')
          return your_weapon

        else:
          print('I don\'t even know what you are saying...')
          continue
    
#player_weapon = player_weapon_selection()
#print('THE PLAYER WEAPON VALUE IS: ' + str(player_weapon)) # FOR DEBUGGING PURPOSES

## COMPUTER WEAPON SELECTION ##

def computer_weapon_selection():
    result = randomizer(random_phrase_dictionary['opponent_selection'])
    result = result[0]
    return result 

#cp_weapon = computer_weapon_selection() # THIS RETURNS THE INDEX NUMBER FOR WEAPON

# print('THE COMPUTER WEAPON VALUE IS: ' + str(cp_weapon)) # FOR DEBUGGING PURPOSES

#print(list(random_phrase_dictionary['opponent_selection'].keys())[0][1])


## WEAPON COMPARISON ##
def weapon_comparison(player_weapon, cp_weapon):

    # DEBUG VARIABLES
    #player_weapon = 3
    #cp_weapon = 0
    #you_win = False

    # IMPORTANT! - INCLUDE => computer_weapon_selection() and player_weapon_selection

    if player_weapon == 3: # player cheats by using gun
        while True:
            print('bang \n')

    elif player_weapon == cp_weapon: # draw condition
        input('It is a draw. :| \n')
        return False

    elif cp_weapon == 0 and player_weapon == 2: # player loses to rock
        input('You lose. :( \n')
        return False

    elif player_weapon == 0 and cp_weapon == 2: # player wins with rock
        input('You win. :) \n')
        return True

    elif player_weapon > cp_weapon:
        input('You win. :) \n')
        return True

    else:
        input('You lose. :( \n')
        return False

    return bool(you_win)

#print(str(player_weapon) + ' vs ' + str(cp_weapon)) # FOR DEBUGGING RUN

#are_ya_winning_son = weapon_comparison(player_weapon, cp_weapon)
#print(are_ya_winning_son) # FOR DEBUGGING RUN

## YOU WIN OR LOSE ##

def results_narration(results):
    if results == 0:
        losing_result = randomizer(random_phrase_dictionary['losing_weights'])
        print(losing_result)
        pass

    else:
        winning_result = randomizer(random_phrase_dictionary['winning_weights'])
        print(winning_result)
        pass

    wanna_play_again()

#results_narration(bool(are_ya_winning_son)) # FOR DEBUGGING RUN - RETURNS RESULT NARRATION

## PLAY AGAIN FUNCTION ##

def wanna_play_again():
    play_again_friend = True

    while play_again_friend == True:

        again = input('Wanna play again? (Y/N) : ').lower() # note: input gives a string indexed at 0

        if again == 'yes' or again == 'y':
            print('\nOkay, you want to play again.\
            \n\n*************************************')
            play_again_friend = False

        elif again == 'no' or again == 'n':
            print('\nOkay, you don\'t want to play anymore. Goodbye.')
            game_start == False
            quit()

        else:
            print('I didn\'t understand that... Try again.')

#wanna_play_again() # FOR DEBUGGING RUN


def rps_game(game_start):

    while game_start == True:
        print('\nWelcome to this normal Rock Paper Scissor Game.\n')

        ## MAKE A SELECTION ##
        make_a_selection_narration() # purely narration
        player_weapon = player_weapon_selection()
        cp_weapon = computer_weapon_selection()
        
        ## IT IS TIME TO DUEL ##
        input("On your mark...\n")
        input(' __  _  /_\n//_//_ /\ \n')
        input(" _  _  _  _  _\n /_//_|/_//_'/ \n/     /      ")
        input(" _ _  .  _  _ _  _  _\n_\ /_ / _\ _\ /_// _\ \n")


        ## COMPARISON OF CP AND PLAYER RESULTS
        # I know the below code is a disaster, ok - I'm not fixing it rn - it worked
        print('Your ' +\
            list(random_phrase_dictionary['opponent_selection'].keys())[player_weapon][1]\
            + ' vs ' + \
            'computer\'s ' + list(random_phrase_dictionary['opponent_selection'].keys())[cp_weapon][1]\
            + '\n')
        are_ya_winning_son = weapon_comparison(player_weapon, cp_weapon)

        ## RESULTS
        results_narration(bool(are_ya_winning_son))

rps_game(game_start)