import requests
from bs4 import BeautifulSoup
import sys

# https://insights.blackcoffer.com/streamlined-integration-interactive-brokers-api-with-python-for-desktop-trading-application/
url = sys.argv[1]
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the main content of the article
article_content = soup.find('div', class_='td-post-content tagdiv-type')

article_text = ""
for i in article_content:
    article_text += '\n' + i.text

# print(article_text)

f = open(f"extracted_text_files/{sys.argv[2]}.txt", "a")
f.write(article_text)
f.close()