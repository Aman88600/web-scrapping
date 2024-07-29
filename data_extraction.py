import requests
from bs4 import BeautifulSoup
import sys

# https://insights.blackcoffer.com/streamlined-integration-interactive-brokers-api-with-python-for-desktop-trading-application/
url = sys.argv[1]
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the main content of the article
article_content = soup.find_all('div', class_='td-theme-wrap')

for i in article_content:
    title_text = i.article.find('div', class_='td-full-screen-header-image-wrap').find('div', class_='td-container td-post-header').find('div', class_='td-parallax-header').header.h1.text

f = open(f"extracted_text_files/{sys.argv[2]}.txt", "w")
f.write(title_text)
f.close()