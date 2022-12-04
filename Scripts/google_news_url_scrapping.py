import requests
from bs4 import BeautifulSoup

TOPICS_URL = "https://news.google.com/rss/topics/"
SPORTS_TOPIC_ID = "CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp1ZEdvU0FtVnpHZ0pGVXlnQVAB"
SECTIONS = "?hl=es&gl=ES&ceid=ES%3Aes/"
FOOTBALL_SECTION_ID = "CAQiR0NCQVNMd29JTDIwdk1EWnVkR29TQW1WekdnSkZVeUlPQ0FRYUNnb0lMMjB2TURKMmVEUXFDd29KRWdkR3c3cDBZbTlzS0FBKioIAComCAoiIENCQVNFZ29JTDIwdk1EWnVkR29TQW1WekdnSkZVeWdBUAFQAQ"
FLAGS = "?hl=es&gl=ES&ceid=ES%3Aes"

TOPICS_IDS = [
    SPORTS_TOPIC_ID]

SPORTS_SECTIONS = [
    FOOTBALL_SECTION_ID]

def main():
    url = f"{TOPICS_URL}{SPORTS_TOPIC_ID}{SECTIONS}{FOOTBALL_SECTION_ID}"
    try:
        page = requests.get(url)
    except:
        print(f"Couldn't get url: {url}")
        
    soup = BeautifulSoup(page.content, 'xml')
    link = soup.find_all('link')
    for i in link:
        print(i.text)
        
if __name__ == "__main__":
    main()