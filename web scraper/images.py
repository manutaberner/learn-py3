from PIL import Image
from bs4 import BeautifulSoup
import requests
from io import BytesIO

def StartSearch():
    search = input('Enter search term:')
    params = {'q': search}
    r = requests.get('https://www.bing.com/images/search', params = params)

    soup = BeautifulSoup(r.text, 'html.parser')
    links = soup.findAll('a',{'class': 'thumb'})

    for item in links:
        img_obj = requests.get(item.attrs['href'])
        print('Getting:', item.attrs['href'])
        title = item.attrs['href'].split('/')[-1]
        img = Image.open(BytesIO(img_obj.content))

        img.save('./web scraper/kk/' + title, img.format)

    StartSearch()

StartSearch()
