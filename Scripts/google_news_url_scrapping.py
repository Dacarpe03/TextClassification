import requests
from bs4 import BeautifulSoup
import pandas as pd

TOPICS_URL = "https://news.google.com/rss/topics/"
SPORTS_TOPIC_ID = "CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp1ZEdvU0FtVnpHZ0pGVXlnQVAB/"
SECTIONS = "sections/"
FOOTBALL_SECTION_ID = "CAQiR0NCQVNMd29JTDIwdk1EWnVkR29TQW1WekdnSkZVeUlPQ0FRYUNnb0lMMjB2TURKMmVEUXFDd29KRWdkR3c3cDBZbTlzS0FBKioIAComCAoiIENCQVNFZ29JTDIwdk1EWnVkR29TQW1WekdnSkZVeWdBUAFQAQ"
BASKET_SECTION_ID = "CAQiS0NCQVNNZ29JTDIwdk1EWnVkR29TQW1WekdnSkZVeUlPQ0FRYUNnb0lMMjB2TURFNGR6Z3FEZ29NRWdwQ1lXeHZibU5sYzNSdktBQSoqCAAqJggKIiBDQkFTRWdvSUwyMHZNRFp1ZEdvU0FtVnpHZ0pGVXlnQVABUAE"
TENIS_SECTION_ID = "CAQiRENCQVNMUW9JTDIwdk1EWnVkR29TQW1WekdnSkZVeUlPQ0FRYUNnb0lMMjB2TURkaWN6QXFDUW9IRWdWVVpXNXBjeWdBKioIAComCAoiIENCQVNFZ29JTDIwdk1EWnVkR29TQW1WekdnSkZVeWdBUAFQAQ"
F1_SECTION_ID = "CAQiS0NCQVNNZ29JTDIwdk1EWnVkR29TQW1WekdnSkZVeUlPQ0FRYUNnb0lMMjB2TURKNGVqSXFEZ29NRWdwR3c3TnliWFZzWVNBeEtBQSoqCAAqJggKIiBDQkFTRWdvSUwyMHZNRFp1ZEdvU0FtVnpHZ0pGVXlnQVABUAE"
FLAGS = "?hl=es&gl=ES&ceid=ES%3Aes"

TOPICS_IDS = [
    SPORTS_TOPIC_ID]

SPORTS_SECTIONS = [
    FOOTBALL_SECTION_ID,
    BASKET_SECTION_ID,
    TENIS_SECTION_ID,
    F1_SECTION_ID]


DATA_FOLDER = "../Datos/"
URL_FILE_NAME = f"{DATA_FOLDER}urls.csv"

def main():
    # session = requests.Session()
    # response = session.get("https://news.google.com/__i/rss/rd/articles/CBMiVWh0dHBzOi8vd3d3Lm1hcmNhLmNvbS9mdXRib2wvbXVuZGlhbC9jcm9uaWNhLzIwMjIvMTIvMDMvNjM4YjY1YmMyNjhlM2VmNzI1OGI0NThhLmh0bWzSAVVodHRwczovL2FtcC5tYXJjYS5jb20vZnV0Ym9sL211bmRpYWwvY3JvbmljYS8yMDIyLzEyLzAzLzYzOGI2NWJjMjY4ZTNlZjcyNThiNDU4YS5odG1s?oc=5")
    # soup = BeautifulSoup(response.text, 'html.parser')
    # article = soup.find('div', {"class":"ue-c-article__body"})
    # for i in article.find_all('p'):
    #     print(i.text)
    sports_urls = select_sports_urls()
    save_urls_to_dataframe(sports_urls, "sports")
    
    
def select_sports_urls():
    urls = []
    for sport_section in SPORTS_SECTIONS:
        print("*********")
        gnews_url = f"{TOPICS_URL}{SPORTS_TOPIC_ID}{SECTIONS}{sport_section}{FLAGS}"
        response = requests.get(gnews_url)
        soup = BeautifulSoup(response.text, "xml")
        news = soup.find_all("item")
                
        response = requests.get(gnews_url)
        soup = BeautifulSoup(response.text, "xml")
        news = soup.find_all("item")
        i = 0
        retrieved = 0
        while retrieved < 15 and i < len(news)-1:
            title = news[i].find('title')
            link = news[i].find('link')
            print("Quieres la noticia con titulo: " + title.text)
            y = input("(y/n): ")
            if y == "y":
                urls.append(["sports", title.text,link.text])
                retrieved += 1
            print("Noticias: " + str(retrieved) + "/15" )
            i+=1
        
    return urls

def save_urls_to_dataframe(urls, category):
    previous_df = pd.read_csv(URL_FILE_NAME, index_col=0)
    df = pd.DataFrame(urls, columns=["category","title","link"])
    
    new_df = pd.concat([previous_df, df], ignore_index=True)
    new_df.to_csv(URL_FILE_NAME)
    
if __name__ == "__main__":
    main()