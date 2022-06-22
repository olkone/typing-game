import random
import time
from termcolor import colored
from funcs import add_phrases, ready_up, type_on

DASH = "-"*70
DOUBLE = "="*70

print(colored(f"{DASH}\nHow fast can you type?\n\
A randomly generated quote will appear.\n\
It's your job to accurately type the quote as fast as you can.\n{DASH}", 'yellow'))

player_name = input("What is your name? ")
print(f'Welcome, {player_name}.\n{DASH}')

print("Generating phrases...")
phrase_list = add_phrases()

round_num = 0
score_list = []

while ready_up(player_name, score_list):
    seed = random.randint(1, (2**99))
    round_num += 1

    start_time = time.perf_counter()
    print(colored(f"{DOUBLE}\nROUND {round_num}\n{DOUBLE}", 'yellow'))

    type_on(round_num, phrase_list, score_list, seed, start_time)
