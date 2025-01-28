import random 

def roll_dice():
    return random.choice([1,2,3,4,5,6])

def attacker_dice():
    dice_rolls = sorted([roll_dice(), roll_dice(), roll_dice()], reverse= True)
    return dice_rolls

def defender_dice():
    return sorted([roll_dice(), roll_dice()], reverse=True)

win_dict = {
    'attacker_win': 0,
    'tie': 0,
    'defender_win': 0
}

for i in range(1000000):
    a_dice = attacker_dice()
    d_dice = defender_dice()
    
    fight_1, fight_2 = 0, 0
    if a_dice[0] > d_dice[0]:
        fight_1 = 1
    if a_dice[1] > d_dice[1]:
        fight_2 = 1

    if (fight_1 + fight_2) == 2:
        win_dict['attacker_win'] += 1
    elif (fight_1 + fight_2) == 1:
        win_dict['tie'] += 1
    else:
        win_dict['defender_win'] += 1

win_dict
