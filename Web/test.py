import requests
from bs4 import BeautifulSoup

#req=requests.get('https://doi.org/10.1103/PhysRevLett.124.041803')
req=requests.get('https://doi.org/10.1007/JHEP01(2020)036')
html = req.text
soup = BeautifulSoup(html,'html.parser')
a = soup.find_all("meta",{"name":"citation_journal_title"})[0]['content']

print(a)
