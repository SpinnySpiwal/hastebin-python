

import requests, sys
from bs4 import BeautifulSoup


def Download(link, filename):
    url = 'https://hastebin.app/' + str(link)

    r = requests.get(url)
    r = str(r.text)

    soup = BeautifulSoup(r, 'html.parser')
    code = soup.find('code')
    code = code.getText()

    FILE = open(filename, 'w')
    FILE.write(code)
    FILE.close()



def Upload(file_text):
    url = 'https://hastebin.app/paste'
    data = {'content': file_text}

    r = requests.post(url, json = data)
    
    if r.status_code == 200:
        link = 'https://hastebin.app/' + str(r.text)

        print(link)

        return link
    else:
        print(r.status_code)



def ParseFile(document):
    file = open(document, 'r')
    file_contents = str(file.read())

    return file_contents



if __name__ == '__main__':
    try:
        mode = sys.argv[1]
        document = sys.argv[2]
    except:
        print('No document specified')
        quit()

    
    if mode == '-u':
        file_contents = ParseFile(document)
        Upload(file_contents)
    elif mode == '-d':
        try:
            filename = sys.argv[3]
        except:
            filename = 'file_' + document

        Download(document, filename)


