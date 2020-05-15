import wget

f1 = open("./paper_url.txt","r")
f2 = open("./normal_doi_list.txt","r")

cnt = 1

while 1:
    pdf_url = f1.readline()
    file_name = f2.readline()
    if not pdf_url: break
    wget.download(pdf_url,"./paper/"+str(cnt)+".pdf")
    cnt+=1

f1.close()
f2.close()
