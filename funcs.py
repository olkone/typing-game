import bs4, lxml, random, requests, sys, time

dash = "-"*70
double = "="*70

def add_phrases():

    phrase_list = []
    url = "http://quotes.toscrape.com/page/{}/"

    # There are 10 pages of quotes
    # Loop through each page, scrape html text attributes
    for page in range(1,11):
        scrape_url = url.format(page)
        result = requests.get(scrape_url)
        soup = bs4.BeautifulSoup(result.text, "lxml")

        # In each page, loop through each text element to scrape quote,
        # then add quotes to phrase_list
        for quote in soup.find_all(attrs=('text')):
            phrase_list.append(quote.text)

    return phrase_list
        
def random_phrase(seed, phrase_list):
    random.seed(seed)
    return random.choice(phrase_list)[1:-1]

def ready_up(player_name):

    game_on = False
    typing = True
    round_num = 0
    ready = ''

    while ready != 'yes' or ready != 'no':
        ready = input(f'{player_name}, are you ready to play? Yes or No: ').lower()

        if ready == 'no' or ready == 'n':
            game_on = False
            print(f"Thank you for playing. Goodbye.\n{double}")
            sys.exit()
        
        elif ready == 'yes' or ready == 'y':
            game_on = True
            return game_on
        
        else:
            print(f'Invalid input. Try again.\n{dash}')

def type_on(player_name, round_num, match_phrase, player_input, start_time):
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
        print("Quitting application. Goodbye.")
        sys.exit()

    else:
        print("Incorrect input. Try again!")
        return player_name, (round_num - 1), match_phrase, player_input, start_time, player_input
