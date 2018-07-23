# Score categories
# Change the values as you see fit
YACHT = 'yacht'
ONES = 'ones'
TWOS = 'twos'
THREES = 'threes'
FOURS = 'fours'
FIVES = 'fives'
SIXES = 'sixes'
FULL_HOUSE = 'full_house'
FOUR_OF_A_KIND = 'four_of_a_kind'
LITTLE_STRAIGHT = 'little_straight'
BIG_STRAIGHT = 'big_straight'
CHOICE = 'choice'


def score(dice, category):
    other_categories = {FULL_HOUSE: full_house(dice), 
                     FOUR_OF_A_KIND: four_of_a_kind(dice), 
                     LITTLE_STRAIGHT: little_straight(dice), 
                     BIG_STRAIGHT: big_straight(dice), 
                     CHOICE: choice(dice), 
                     YACHT: yacht(dice)}
    if category == ONES or category == TWOS or category == THREES or category == FOURS or category == FIVES or category == SIXES:
        return first_six_categories(dice, category)
    
    else:
        result = other_categories[category]
        return result
    

def first_six_categories(dice, category):
    number_map = {ONES: sum(filter(lambda x: x == 1, dice)),
                         TWOS: sum(filter(lambda x: x == 2, dice)),
                         THREES: sum(filter(lambda x: x == 3, dice)),
                         FOURS: sum(filter(lambda x: x == 4, dice)),
                         FIVES: sum(filter(lambda x: x == 5, dice)),
                         SIXES: sum(filter(lambda x: x == 6, dice))}
    return number_map[category]

def full_house(dice):
    three_of_a_kind_index = 0
    two_of_a_kind_index = 0
    possible_values = [0]*6
    
    for die in dice:
        possible_values[die-1] += 1
    
    three_of_a_kind_index_list = [i for i,v in enumerate(possible_values) if v == 3]
    two_of_a_kind_index_list = [i for i,v in enumerate(possible_values) if v == 2]

    if len(two_of_a_kind_index_list) > 1 or len(two_of_a_kind_index_list) == 0 or len(three_of_a_kind_index_list) == 0:
        return 0
    
    three_of_a_kind_index = three_of_a_kind_index_list[0]+1
    two_of_a_kind_index = two_of_a_kind_index_list[0]+1

    return three_of_a_kind_index*3 + two_of_a_kind_index*2

def four_of_a_kind(dice):
    four_of_a_kind_index = 0
    possible_values = [0]*6
    
    for die in dice:
        possible_values[die-1] += 1
    
    four_of_a_kind_index_list = [i for i,v in enumerate(possible_values) if v >= 4]

    if len(four_of_a_kind_index_list) == 0:
        return 0

    four_of_a_kind_index = four_of_a_kind_index_list[0] + 1

    return four_of_a_kind_index*4

def little_straight(dice):
    dice.sort()
    if dice[0] != 1 or dice[4] != 5: return 0
    prev = 0
    for die in dice:
        if prev is not 0:
            if prev >= die:
                return 0
        prev = die
    return 30

def big_straight(dice):
    dice.sort()
    if dice[0] != 2 or dice[4] != 6: return 0
    prev = 0
    for die in dice:
        if prev is not 0:
            if prev >= die:
                return 0
        prev = die
    return 30

def choice(dice):
    return sum(dice)

def yacht(dice):
    dice_set = set(dice)
    if(len(dice_set) > 1): return 0
    else: return 50