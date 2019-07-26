#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 11:16:15 2019

@author: lavanyasingh
"""

import requests
from bs4 import BeautifulSoup
import csv
import os
os.chdir(os.path.dirname(os.getcwd()) + "/data")

def get_sources():
    page = 'http://www.inkdrop.net/news/'
    response = requests.get(page)
    soup = BeautifulSoup(response.text, 'html.parser')
    tables = soup.find_all("table", { "class" : "tableOuter" })
    sources = []
    for table in tables:
        rows = table.find_all('tr')
        for row in rows:
            data = row.find_all('td')
            country = data[0].get_text().split(' ')[0]
            url = data[2].find('a').get('href')
            sources.append({'url': url, 'country': country, 'title': "", 
                            'language': "", 'type': ""})
    return sources

def write_sources():
    sources = get_sources()
    with open('inkdrop_sources.csv', mode = 'w') as f:
        w = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        w.writerow(['country', 'source url', 'title', 'language', 'type'])
        for source in sources:
            w.writerow([source['country'], source['url'], source['title'], 
                        source['language'], source['type']])
            
if __name__ == '__main__':
    print(len(write_sources()))