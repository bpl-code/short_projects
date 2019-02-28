#printArticles.py
#This program prints out all the articles from the home page of NY Times

import requests
r = requests.get('https://api.github.com/events')