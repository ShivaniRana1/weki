import requests
from bs4 import BeautifulSoup
import pandas as pd

BASE_URL = "https://en.wikipedia.org/wiki/"
word =  input("Word You are searching??")
url = BASE_URL+word
page = requests.get(url)


soup = BeautifulSoup(page.content, 'html.parser')

 


project_href = [i['href'] for i in soup.find_all('a', href=True)]


df = pd.DataFrame(project_href, columns=[word])
df.to_csv('list.csv', index=False)

