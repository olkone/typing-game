import random, time
from funcs import random_phrase, ready_up, add_phrases, type_on

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

    typing = True

    type_on(player_name, round_num, match_phrase, player_input, start_time)
            