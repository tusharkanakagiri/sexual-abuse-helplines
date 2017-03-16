from pprint import pprint
from bs4 import BeautifulSoup
import urllib.request
import pickle

r = urllib.request.urlopen('http://global.umn.edu/travel/assault/#/3').read()

soup =BeautifulSoup(r)

letters = soup.find_all("div")

heading = letters[17].find_all("p")

pprint(heading)
