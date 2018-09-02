import urllib.request
from bs4 import BeautifulSoup
import os
import csv

with open('foodList.csv', newline='') as f:
    reader = csv.reader(f)
    foods = list(reader)

for item in foods:
    item = item[0]
    folder = './{}s'.format(item)
    url = 'https://pixabay.com/en/photos/?q={}&hp=&image_type=all&order=popular&cat=&min_width=&min_height='.format(item)
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')

    print(soup.title.text)

    i = 0
    if not os.path.exists(folder):
        os.makedirs(folder)

    for link in soup.findAll('div', {'class':'item'}):
        for image in soup.findAll('img'):
            link = image.get('data-lazy')
            if link is not None:
                file = open('{}/{}-{}'.format(folder, item, i) + '.jpg', 'wb')
                file.write(urllib.request.urlopen(link).read())
                file.close()
                i += 1
        if i >= 200:
            break






