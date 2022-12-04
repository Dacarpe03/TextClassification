# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 20:05:39 2022

@author: Daniel
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

DATA_FOLDER = "../Datos/"
URL_FILE_NAME = f"{DATA_FOLDER}urls.csv"


def main():
    news_df = pd.read_csv(URL_FILE_NAME, index_col=0)
    
    for index, row in news_df.iterrows():
        title = row["title"]
        link = row["link"]
        text = scrape_text_from_link(title, link)
        print("========")
        print(link)
        print(text)
        input("Press enter for next...")

def scrape_text_from_link(title, link):
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')
    article = soup.find('article')
    if article == None:
        print("Error, no se puede leer la noticia")
        return None
    full_text = []
    for parragraph in article.find_all('p'):
        full_text.append(parragraph.text)
    return '\n'.join(full_text)

def show_sources(news_df):
    sources = []
    for title in news_df["title"]:
        sources.append(title.split('-')[-1:][0])
    
    print(sources)
    my_set = set(sources)
    for s in my_set:
        print(s)
if __name__ == "__main__":
    main()