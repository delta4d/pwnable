#!/usr/bin/env python3

import os

from bs4 import BeautifulSoup
from bs4.element import *
import requests

PREFIX = "http://pwnable.kr/"
URL = PREFIX + "play.php"

result = requests.get(URL)
soup = BeautifulSoup(result.content, "html.parser")
section = soup.find(class_='color-1')
current_title = ""

for child in section.children:
    if isinstance(child, NavigableString):
        if child[0] == '[':
            current_title = child[1:-1].replace("'", '').replace(' ', '')
            try:
                os.mkdir(current_title)
            except:
                pass
    elif isinstance(child, Tag):
        if child.name == 'figure':
            src = PREFIX + child.find('img')['src']
            img = current_title + '/' + src.split('/')[-1]
            response = requests.get(src, stream=True)
            with open(img, "bw") as f:
                for chunk in response:
                    f.write(chunk)
            print(img + ' ✔')
