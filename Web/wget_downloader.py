import wget

f1 = open("./test_url.txt","r")
f2 = open("./test_list.txt","r")

while 1:

    pdf_url = f1.readline()
    attribute = f2.readline()

    if not attribute: break

    file_name = "_".join(attribute.split(","))
    file_name = "_".join(file_name.split(" "))
    file_name = "".join(file_name.split("/"))
    file_name = file_name.rstrip('\n')
    wget.download(pdf_url,"./paper/"+file_name+".pdf")

f1.close()
f2.close()
