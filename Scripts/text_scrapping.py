# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 20:05:39 2022

@author: Daniel
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

from os.path import exists

DATA_FOLDER = "../Datos/"
URL_FILE_NAME = f"{DATA_FOLDER}urls.csv"


def main():
    news_df = pd.read_csv(URL_FILE_NAME, index_col=0)
    # news_df = news_df[news_df.category=="health"]
    # news_df = news_df[news_df.index > 30]
    
    last_category = "score"
    count = 1
    for index, row in news_df.iterrows():
        category = row["category"]
        if(last_category != category):
            count = 1
        title = row["title"]
        link = row["link"]
        
        print("========")
        print("Link: \n", link)
        text = scrape_text_from_link(title, link)
        print(text)
        
        save_text(category, text, count)
        last_category = category
        count += 1
        
        input("Press enter for next...")


def save_text(category, text, count):
    file_name = f"{DATA_FOLDER}{category}/{category}_{count}.txt"
    if not exists(file_name):
        with open(file_name, "w") as f:
            if text is not None:
                f.write(text)


def scrape_text_from_link(title, link):
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')
    article = soup.find('article')
        
    if article == None:
        print("Error, no se puede leer la noticia")
        return None
    
    for fig in article.select('figure'):
        fig.extract()
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