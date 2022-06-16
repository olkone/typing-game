import bs4, lxml, random, requests, sys, time

dash = "-"*70
double = "="*70

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

        for quote in soup.find_all(attrs=('text')):
            phrase_list.append(quote.text)

    return phrase_list
        
def random_phrase(seed, phrase_list):
    '''
    Create a random seed;
    choose a random phrase from the phrase list
    '''
    random.seed(seed)
    return random.choice(phrase_list)[1:-1]

def ready_up(player_name):
    '''
    Asks player confirmation to continue
    '''
    ready = ''

    while ready != 'yes' or ready != 'no':
        ready = input(f'{player_name}, are you ready to play? Yes or No: ').lower()

        if ready == 'no' or ready == 'n':
            print(f"Thank you for playing. Goodbye.\n{double}")
            sys.exit()
        
        elif ready == 'yes' or ready == 'y':
            return True
        
        else:
            print(f'Invalid input. Try again.\n{dash}')

def type_on(player_name, round_num, phrase_list, seed, start_time):

    seed += 1

    player_input = input(f"{random_phrase(seed, phrase_list)}\n{dash}\n")
    match_phrase = random_phrase(seed, phrase_list)

    word_count = len(match_phrase.split(' '))
    score_list = []
    prev_round = 1 - round_num

    if player_input == match_phrase:
        end_time = time.perf_counter()
        delta_time = end_time - start_time
        wpm = word_count/(delta_time/60)
        score_list.append(wpm)

        print(f"{dash}\nCorrect!\nYour time: {(round(delta_time,3))} seconds\nWords per minute: {round(wpm,3)}\n{dash}")

        if round_num > 1:
            pass
            # print(f"Previous WPM: {score_list[prev_round]}")
        typing = False
    
    elif player_input.lower() == 'quit':
        print("Quitting application. Goodbye.")
        sys.exit()

    else:
        print(f"{dash}\nIncorrect input. Try again!\n{dash}")
        type_on(player_name, round_num, phrase_list, seed-1, start_time)
