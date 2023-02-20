import random

def wanna_play():
    while True:
        #for some reason when I did while user_want != 'no' or 'yes' it just entered the loop anyway, so this way works 100%
        user_want = input('Wanna play some tic tac toe? \n enter yes to play and no to stop! \n').lower()
        if user_want == 'yes' :
            user_want = True # you can just do return True rather than adding the break each time
            break
        elif  user_want == 'no':
            user_want = False
            break
    return user_want

def identify_players():
    player_one = input('Please enter your name, you will play as X! \n')
    player_two = input('Please enter your name, you will play as O! \n')

    player_one = player_one
    player_two = player_two

    return player_one, player_two

def display_board(choice_1,choice_2):
    choice_dict = {
             't_l': ' ',
             't_m' : ' ',
             't_r' : ' ',
             'm_l' : ' ',
             'm_m' : ' ',
             'm_r' : ' ',
             'b_l' : ' ',
             'b_m' : ' ',
             'b_r' : ' '
        }

    for choice in choice_1:
        choice_dict[choice] = 'X'
    for choice in choice_2:
        choice_dict[choice] = 'O'
    return print(f'''
        *************
        * {choice_dict['t_l']} * {choice_dict['t_m']} * {choice_dict['t_r']} *
        * {choice_dict['m_l']} * {choice_dict['m_m']} * {choice_dict['m_r']} *
        * {choice_dict['b_l']} * {choice_dict['b_m']} * {choice_dict['b_r']} *
        *************
        
        ''')

def whos_first_turn():
    turn = 0
    shuffle =  random.randint(1,2)
    return shuffle

def switch_turn(f_turn):
    turn = f_turn
    if turn == 1 :
        turn = 2
    else:
        turn = 1
    return turn

def play_a_turn(turn,choice_1,choice_2):
    all_choices = ['t_l','t_m','t_r','m_l','m_m','m_r','b_l','b_m','b_r']

    for choice in choice_1:
        if choice in all_choices:
            all_choices.remove(choice)
    for choice in choice_2:
        if choice in all_choices:
            all_choices.remove(choice)
    if len(all_choices) == 0:
        return False
    while True:
        string_list = ','.join(all_choices)
        choice = input(f'Please enter your choice for this turn! you can choose: \n turns available: {string_list} \n')
        if choice in all_choices :
            if turn == 1:
                choice_1.append(choice)
                break
            else:
                choice_2.append(choice)
                break


    return choice_1,choice_2

def check_if_win(choice_1,choice_2):
    if len(choice_1) < 3 and len(choice_2)< 3:
       return False,''
    if len(choice_1) > 2:
        # do you remember what we explained regardign  the comments? for each comment you can take the corresponding code and extract it to function
        # check line win
        if 't_l' in choice_1 and 't_m' in choice_1 and 't_r' in choice_1:
            return True,'Player one'
        elif 'm_l' in choice_1 and 'm_m' in choice_1 and 'm_r' in choice_1:
            return True,'Player one'
        elif 'b_l' in choice_1 and 'b_m' in choice_1 and 'b_r' in choice_1:
            return True,'Player one'

            # check diagonal win
        elif 't_l' in choice_1 and 'm_m' in choice_1 and 'b_r' in choice_1:
            return True,'Player one'
        elif 't_r' in choice_1 and 'm_m' in choice_1 and 'b_l' in choice_1:
            return True,'Player one'

            # check height win
        elif 't_r' in choice_1 and 'm_r' in choice_1 and 'b_r' in choice_1:
            return True,'Player one'
        elif 't_l' in choice_1 and 'm_l' in choice_1 and 'b_l' in choice_1:
            return True,'Player one'
        elif 't_m' in choice_1 and 'm_m' in choice_1 and 'b_m' in choice_1:
            return True,'Player one'
    if len(choice_2) > 2:
            # check line win
        if 't_l' in choice_2 and 't_m' in choice_2 and 't_r' in choice_2:
            return True,'Player two'
        elif 'm_l' in choice_2 and 'm_m' in choice_2 and 'm_r' in choice_2:
            return True,'Player two'
        elif 'b_l' in choice_2 and 'b_m' in choice_2 and 'b_r' in choice_2:
            return True,'Player two'

            # check diagonal win
        elif 't_l' in choice_2 and 'm_m' in choice_2 and 'b_r' in choice_2:
            return True,'Player two'
        elif 't_r' in choice_2 and 'm_m' in choice_2 and 'b_l' in choice_2:
            return True,'Player two'

                # check height win
        elif 't_r' in choice_2 and 'm_r' in choice_2 and 'b_r' in choice_2:
            return True,'Player two'
        elif 't_l' in choice_2 and 'm_l' in choice_2 and 'b_l' in choice_2:
            return True,'Player two'
        elif 't_m' in choice_2 and 'm_m' in choice_2 and 'b_m' in choice_2:
            return True,'Player two'

    return False , ''


def time_to_play():
    if not wanna_play():
        print('Youre no fun at parties are you')
        return False
    players = identify_players()
    player_one = players[0]
    player_two = players[1]
    choice_1 = []
    choice_2 = []
    turn = whos_first_turn()

    if turn == 1:
        print(f'{player_one} goes first!')
    else:
        print(f'{player_two} goes first!')

    while True:
        display_board(choice_1,choice_2)
        win = check_if_win(choice_1,choice_2)
        if win[0] == True:
            break
        if turn == 1:
            print(f'{player_one} goes now')
        else:
            print(f'{player_two} goes now')
        choices = play_a_turn(turn,choice_1,choice_2)
        if choices == False:
            break
        choice_1 = choices[0]
        choice_2 = choices[1]
        turn = switch_turn(turn)
    if win[1] == 'Player one':
        winner = player_one
    else:
        winner = player_two
    if win[0] == True:
        print(f'winner winner chicken dinner \n congrats {winner}')
    else:
        print('No more moves! try again :)')

time_to_play()
