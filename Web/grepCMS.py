import requests
from bs4 import BeautifulSoup

from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open
import urllib.request

def read_pdf_file(pdfFile):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)

    process_pdf(rsrcmgr, device, pdfFile)
    device.close()

    content = retstr.getvalue()
    retstr.close()
    return content

pdf_file = open("./publi.pdf", "rb")

contents = read_pdf_file(pdf_file)
arxiv = contents.split("arXiv:")
num_list = []

for i in arxiv[1:125]:
    a = i.split('.')
    c = '.'.join(a[0:2])
    num_list.append(c)

#print(num_list)

#print(type(contents))
pdf_file.close()

#link='https://arxiv.org/abs/1809.08602'
#link='https://arxiv.org/abs/1711.03573' # non doi

cnt=0
filtered_list=[]

for link_num in num_list:
    link = 'https://arxiv.org/abs/2002.06398'
    #link = 'https://arxiv.org/abs/' + link_num
    
    #cnt += 1


    req=requests.get(link)
    html = req.text
    soup = BeautifulSoup(html,'html.parser')
    #print(soup)

    #isDOI=True

    a_tags = soup.select("td > a")
    
    data_doi = str()
    href = str()

    for a_tag in a_tags:
        if 'doi.org'in a_tag['href']:
            data_doi = a_tag['data-doi']
            href = a_tag['href']
            doi_req = requests.get(href)
            print(doi_req)
            doi_html = doi_req.text
            doi_soup = BeautifulSoup(doi_html,'html.parser')
            #journal = soup.select("head > meta")
            print(doi_soup)

    if not data_doi:
        print("There is no DOI")
        #isDOI = False
    else:
        print(data_doi,href)
        #print("DOI: ", isDOI)
        filtered_list.append(link)
        cnt +=1

print(cnt)   