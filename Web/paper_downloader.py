#paper_downloader.py

import requests
from bs4 import BeautifulSoup

f1 = open("./normal_doi_list.txt","r")
f2 = open("./paper_list.txt","w")
f3 = open("./paper_url.txt","w")

attribute_name = ['citation_journal_title','citation_volume','citation_issue','citation_firstpage','citation_date']

while True:

    line = f1.readline()
    if not line: break
    req = requests.get('https://doi.org/'+line)
    html = req.text
    soup = BeautifulSoup(html,'html.parser')

    parse = req.url.split('/')
    paper_url = str()

    attribute=[]
    
    for i in attribute_name:
        if i == 'citation_date':
            if attribute[0]=='Journal of High Energy Physics' or attribute[0]=='The European Physical Journal C':
                attribute.append(soup.find_all("meta",{"name":'citation_lastpage'})[0]['content'])
                attribute.append(soup.find_all("meta",{"name":'citation_online_date'})[0]['content'])
                parse[3] = 'content/pdf'
                paper_url = "/".join(parse)
                break
            else:
                parse[4] = 'pdf'
                paper_url = "/".join(parse)
        attribute.append(soup.find_all("meta",{"name":i})[0]['content'])

    f2.write(",".join(attribute)+"\n")
    f3.write(paper_url+"\n")

f1.close()
f2.close()
f3.close()
