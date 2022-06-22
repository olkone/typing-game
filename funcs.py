import random
import sys
import time
import bs4
import lxml
import requests
from numpy import average
from termcolor import colored

DASH = "-"*70
DOUBLE = "="*70

def add_phrases():
    '''
    Scrape a website of its quotes;
    add quotes to a list
    '''
    phrase_list = []
    url = "http://quotes.toscrape.com/page/{}/"

    # There are 10 pages of quotes to loop through
    for page in range(1,11):
        scrape_url = url.format(page)
        result = requests.get(scrape_url)

        # Gather all elements with the 'text' attribute
        soup = bs4.BeautifulSoup(result.text, "lxml")

        # Loop through all text attributes
        # Append phrase_list with quotes < 30 words long
        for quote in soup.find_all(attrs=('text')):
            if len(quote.text.split()) < 31:
                phrase_list.append(quote.text)

   # Replace ’ and ′ with ' using ASCII values
    phrase_list = [punc.replace(chr(8217), chr(39)).replace(chr(8242), chr(39)) for punc in phrase_list]
    return phrase_list

def random_phrase(seed, phrase_list):
    '''
    Create a random seed;
    choose a random phrase from the phrase list
    '''
    random.seed(seed)
    return random.choice(phrase_list)[1:-1]

def ready_up(player_name, score_list):
    '''
    Asks player confirmation to continue
    '''
    ready = ''

    while ready != 'yes' or ready != 'no':
        ready = input(f'{DASH}\n{player_name}, are you ready to play? Yes or No: ').lower()

        if ready in ['no', 'n']:
            print(f"Thank you for playing. Goodbye.\n{DOUBLE}")
            sys.exit()

        elif ready in ['yes', 'y']:
            return score_list, True

        else:
            print(f'Invalid input. Try again.\n{DASH}')

def type_on(round_num, phrase_list, score_list, seed, start_time):
    '''
    Main gameplay function. Pulls a phrase from phrase_list according to the seed.
    Compares player input to original phrase.
    Calculates and displays WPM stats.
    '''
    seed += 1

    player_input = input(f"{random_phrase(seed, phrase_list)}\n{DASH}\n")
    match_phrase = random_phrase(seed, phrase_list)
    word_count = len(match_phrase.split(' '))

    if player_input == match_phrase:
        delta = time.perf_counter() - start_time
        wpm = word_count/(delta/60)
        score_list.append(round(wpm,3))
        print(colored(f"{DASH}\nCorrect!\n{DASH}",'green'))
        print(colored(f"Your time: {(round(delta,3))} seconds", 'cyan'))
        print(colored(f"Words per minute: {round(wpm,3)}", 'cyan'))

        if round_num > 1:
            print(colored(f"\nPrevious WPM: {score_list[round_num-2]}",'cyan'))
            print(colored(f"Maximum WPM: {max(score_list)}",'cyan'))
            print(colored(f"Average WPM: {round(average(score_list),3)}",'cyan'))

    elif player_input.lower() == 'quit':
        print("Quitting application. Goodbye.")
        sys.exit()

    else:
        print(colored((f"{DASH}\nIncorrect input. Try again!\n{DASH}"), 'red'))
        # seed-1 reverts to previous seed.
        # The player is given the same phrase to try typing again.
        type_on(round_num, phrase_list, score_list, seed-1, start_time)
