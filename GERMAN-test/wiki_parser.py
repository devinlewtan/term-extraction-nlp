#!/usr/bin/python3

from bs4 import BeautifulSoup

def preprocess(text):
    return text.strip()

with open("foreground.txt", "r") as f:

    contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')
    docs = soup.find_all('doc')
    i = 0
    list = open("foreground.list", 'a')
    for doc in docs:
        file_name = doc['title'].replace('/', "").replace(' ', "")

        fi = open(("./foreground/" + file_name + ".txt"), 'w')
        list.write(file_name + ".txt\n")

        file_body = preprocess(doc.get_text())
        fi.write(file_body)

fi.close()
list.close()

