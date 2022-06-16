import random, time
from funcs import  ready_up, add_phrases, type_on

dash = "-"*70
double = "="*70

print(f'\n{dash}' + "\nHow fast can you type?\nA randomly generated quote will appear.\nIt's your job to accurately type the quote as fast as you can.")

player_name = input(f"{dash}\nWhat is your name? ")
print(f'Welcome, {player_name}.\n{dash}')

wrong_type = True       

print("Generating phrases...")
phrase_list = add_phrases()

round_num = 0

while ready_up(player_name):
    seed = random.randint(1, (2**99))
    round_num += 1
    start_time = time.perf_counter()
    print(f"{double}\nROUND {round_num}\n{double}")

    type_on(player_name, round_num, phrase_list, seed, start_time)
    