import requests
from bs4 import BeautifulSoup

def scrape_me(url, print_it=False):
    soup = BeautifulSoup(requests.get(url).text, 'lxml')

    for item in enumerate(soup.find_all('div', class_='card')[:-1]):
        scrape_me.counter += 1
        item_name, item_price = item[1].find('h4', class_='card-title'), item[1].find('h5')
        print('{}). Price: {}, Item Name: {}'.format(scrape_me.counter-10, item_price.text, item_name.text.strip('\n'))) if print_it else None
    
    return soup

scrape_me.counter = 1

base_url = 'https://scrapingclub.com/exercise/list_basic/'

for link in scrape_me(base_url).find('ul', class_='pagination').find_all('a', class_='page-link'):
    scrape_me(base_url + str(link.get('href') if (link.text.isdigit() and int(link.text) is not None) else None), print_it=True)