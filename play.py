import random, time
from funcs import random_phrase, ready_up, add_phrases

dash = "-"*70
double = "="*70

print(f'\n{dash}' + "\nHow fast can you type?\nA randomly generated quote will appear.\nIt's your job to accurately type the quote as fast as you can.")

player_name = input(f"{dash}\nWhat is your name? ")
print(f'Welcome, {player_name}.\n{dash}')

wrong_type = True       

print("Generating phrases...")
phrase_list = add_phrases()

round_num = 0

while ready_up(player_name) is True:
    round_num += 1
    seed = random.randint(1,(9**99))
    print(f"{double}\nROUND {round_num}\n{double}")
    
    start_time = time.perf_counter()
    player_input = input(f"{random_phrase(seed, phrase_list)}\n{dash}\n")
    match_phrase = random_phrase(seed, phrase_list)
    #player_input = input('test ') ## delete later
    #match_phrase = 'test' ## delete later

    typing = True

    while typing:

        word_count = len(match_phrase.split(' '))
        score_list = []
        prev_round = 1 - round_num

        if player_input == match_phrase:
            end_time = time.perf_counter()
            delta_time = end_time - start_time
            wpm = word_count/(delta_time/60)
            score_list.append(wpm)
            print(f"{dash}\nCorrect!\nYour time: {(round(delta_time,3))} seconds")
            print(f"Words per minute: {round(wpm,3)}")
            print(dash)
    
            if round_num > 1:
                pass
               # print(f"Previous WPM: {score_list[prev_round]}")
            typing = False
        
        elif player_input.lower() == 'quit':
            break

        else:
            print("Incorrect input. Try again!")
            typing = False