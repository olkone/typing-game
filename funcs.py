import time, random, bs4, requests, sys

class Phrases():
    
    def __init__(self, seed=42):
        self.seed = seed
        self.phrases = []

    def add_phrases(self):
    
        url = "https://quotes.toscrape.com/page/{}/"

        # There are 10 pages of quotes
        # Loop through each page, scrape html text attributes
        for page in range(1,11):
            scrape_url = url.format(page)
            result = requests.get(scrape_url)
            soup = bs4.BeautifulSoup(result.text, 'lxml')

            # In each page, loop through each text element to scrape quote,
            # then add quotes to phrase_list
            for quote in soup.find_all(attrs=('text')):
                self.phrases.append(quote.text)
    
    def random_phrase(self):
        random.seed(self.seed)
        return random.choice(self.phrases)[1:-1]

def ready_up():

    player_name = input("What is your name? ")
    print(f'PLAYER: {player_name}\n' + '-'*30)

    game_on = False
    typing = True
    round_num = 0
    ready = ''

    while ready != 'yes' or ready != 'no':
        ready = input(f'{player_name}, are you ready to play? Yes or No: ').lower()

        if ready == 'no' or ready == 'n':
            game_on = False
            print("Thank you for playing. Goodbye.")
            sys.exit()
        
        elif ready == 'yes' or ready == 'y':
            game_on = True
            return game_on
        
        else:
            print('Invalid input. Try again.\n' + '-'*30)
