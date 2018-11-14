# -*- coding: utf-8 -*-
"""
This script is to convert html files to text files.
"""

import urllib.request
from bs4 import BeautifulSoup as Soup

soup = Soup(urllib.request.urlopen('file:///C:/Users/Marriane/Documents/GitHub/empath-on-movie-reviews/data/subjectivity_html.tar/subjectivity_html/subjectivity_html/obj/2002/Aankhen.html').read())

text = soup.get_text()
final = text.encode('utf-8') #make sure to encode your text to be compatible
#raw = nltk.clean_html(document)
print(text.encode('utf-8'))
