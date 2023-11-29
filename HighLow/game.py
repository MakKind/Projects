main_logo = '''
  _    _ _       _               
 | |  | (_)     | |              
 | |__| |_  __ _| |__   ___ _ __ 
 |  __  | |/ _` | '_ \ / _ \ '__|
 | |  | | | (_| | | | |  __/ |   
 |_|  |_|_|\__, |_| |_|\___|_|   
 | |        __/ |                
 | |     __|___/    _____ _ __   
 | |    / _ \ \ /\ / / _ \ '__|  
 | |___| (_) \ V  V /  __/ |     
 |______\___/ \_/\_/ \___|_|
'''
vs_logo = '''
         __    
 /\   /\/ _\   
 \ \ / /\ \    
  \ V / _\ \   
   \_/  \__/ 
'''
import random
import gameData
import os

def play_game():
    print(main_logo)
    game_over = False
    score = 0
    Choice_A = random.choice(gameData.data)
    choice_B = random.choice(gameData.data)
    while not game_over:
        if Choice_A == choice_B:
            choice_B = random.choice(gameData.data)
        print(f"Compare A: {Choice_A['name']}, {Choice_A['description']} from {Choice_A['country']}")
        print(vs_logo)
        print(f"Against B: {choice_B['name']}, {choice_B['description']} from {choice_B['country']}")
        guess = input(f"Who has more followers? Type 'A' or 'B': ")
        if guess == 'A':
            if Choice_A['follower_count'] < choice_B['follower_count']:
                game_over = True
            else:
                score += 1
                print(f"You are correct. Your score is {score}")
                choice_B = random.choice(gameData.data)
        elif guess == 'B':
            if Choice_A['follower_count'] > choice_B['follower_count']:
                game_over = True
            else:
                score += 1
                print(f"You are correct. Your score is {score}")
                Choice_A = choice_B
                choice_B = random.choice(gameData.data)
    return score

while input("Do you want to play a game of Higher/Lower? Type 'y' for a new game, 'n' to exit: ") == 'y':
    os.system('cls' if os.name == 'nt' else 'clear')
    score = play_game()
    print(f"Sorry! That is wrong. \n. Final score is {score}")