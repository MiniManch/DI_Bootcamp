import random

def wanna_play():
    while True:
        #for some reason when I did while user_want != 'no' or 'yes' it just entered the loop anyway, so this way works 100%
        user_want = input('Wanna play some tic tac toe? \n enter yes to play and no to stop! \n').lower()
        if user_want == 'yes' :
            user_want = True
            break
        elif  user_want == 'no':
            user_want = False
            break
    return user_want

def identify_players():
    player_one = input('Please enter your name, you will play as X! \n')
    player_two = input('Please enter your name, you will play as O! \n')

    player_one = (player_one,'X')
    player_two = (player_two,'O')

    return player_one, player_two

def display_board(choice_1,choice_2):
    if len(choice_1) == 0 and len(choice_2) == 0:
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
        # choice 1 and choice 2 are dicts where the key is the position and value is defined by the player one or two and is constant.
    else:
        choice_dict = {}
        for choice in choice_1:
            choice_dict[choice] = 'X'
        for choice in choice_2:
            choice_dict[choice] = 'O'
    return choice_dict,(f'''
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
    while True:
        string_list = ','.join(all_choices)
        choice = input(f'Please enter your choice for this turn! you can choose: \n turns available: {string_list}')
        if choice in all_choices :
            if turn == 1:
                choice_1.append(choice)
            else:
                choice_2.append(choice)

    return choice_1,choice_2

def time_to_play():
    