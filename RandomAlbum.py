import requests
from bs4 import BeautifulSoup
import random
import ctypes

url = 'https://pitchfork.com/features/lists-and-guides/the-200-best-albums-of-the-2010s/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')

df = []
for heading in soup.find_all(["h2"]):
    df.append(heading.text)

ctypes.windll.user32.MessageBoxW(0, random.choice(df), "Random Album", 1)
