import  random
from art import vs,logo
from game_data import data
#This is where I pick users info at random
DATA_CHOICE, DATA_CHOICE_2 = random.sample(data, 2)

# This is where I compare user choice either 'a' or 'b'
def compare_choice(choice1):
    if choice1 == 'a' and follower_count > follower_count_2:
        return True
    elif choice1 == 'a' and follower_count < follower_count_2:
        return  False
    elif choice1 == 'b' and follower_count > follower_count_2:
        return False
    elif choice1 == 'b' and follower_count < follower_count_2:
        return True
    else:
        return None


game_over = False
LIVES = 1
while not game_over:
    print(logo)

#This is where I assign each key and their value to a variable, so that I can print it out individually
    name = DATA_CHOICE['name']
    follower_count = DATA_CHOICE['follower_count']
    description = DATA_CHOICE['description']
    country = DATA_CHOICE['country']

    name_2 = DATA_CHOICE_2['name']
    follower_count_2 = DATA_CHOICE_2['follower_count']
    description_2 = DATA_CHOICE_2['description']
    country_2 = DATA_CHOICE_2['country']
# I saved the individuals or companies information here
    user_info_1 = f'compare A: {name}, {description}, {country}'
    user_info_2= f'compare B: {name_2}, {description_2}, {country_2}'

# This is where I printed them out on the console
    print(user_info_1)
    print(vs)
    print(user_info_2)

# This is where I ask user to make a choice
    user_choice = input(f"who has more followers type 'a' or 'b': ").lower()

# This is where I saved the output from my compare function
    compare_output = compare_choice(user_choice)

# This is where I gave conditions to the output of my compare function
    if compare_output:
        print(f'YOU ARE RIGHT!!, YOUR CURRENT SCORE IS {LIVES}')
        DATA_CHOICE = DATA_CHOICE_2
        DATA_CHOICE_2 = random.choice(data)
        LIVES += 1
    elif compare_output == False:
            LIVES -= 1
            print('\n' * 10)
            print(logo)
            print(f'SORRY YOU ARE WRONG, YOUR CURRENT SCORE IS {LIVES}')
            game_over = True












