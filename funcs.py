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
