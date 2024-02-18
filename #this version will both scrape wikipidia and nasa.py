#this version will both scrape wikipidia and nasa 


import requests
import string
from bs4 import BeautifulSoup
import pandas as pd

Enter_input = input("Search: ")
u_i = string.capwords(Enter_input)
lists = u_i.split()
word = "_".join(lists)

url = "https://en.wikipedia.org/wiki/" + word

def wikibot(url):
    url_open = requests.get(url)
    soup = BeautifulSoup(url_open.content, 'html.parser')
    all_data = []  # List to store all scraped data

    # Scrape text content from paragraphs, headings, and article body
    for tag in soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'div']):
        if tag.name not in ['img', 'figcaption', 'table', 'tr', 'th', 'td', 'ul', 'ol', 'li']:
            all_data.append([tag.get_text()])

    return all_data

scraped_data = wikibot(url)
column_names = ['Data']
df = pd.DataFrame(scraped_data, columns=column_names)
df.to_csv(f'{word}.csv', index=False)







