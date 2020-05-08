"""
get https://www.reddit.com/r/FreeEBOOKS/comments/g34xi5/408_free_ebooks_from_springer/
get 408 free ebooks from Springer
"""

import requests
from bs4 import BeautifulSoup


headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}
proxies = {'http':'http://127.0.0.1:1087',
           'https':'http://127.0.0.1:1087'}

def getUrl(url):
    res = requests.get(url,headers=headers,proxies=proxies,timeout=30)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text,'html.parser')
    rxs = soup.find_all('p',class_='_1qeIAgB0cPwnLhDF9XSiJM')
    ulist1 = []
    for i in range(len(rxs)):
        try:
            title = rxs[i].text
            link = rxs[i].select('a')[0]['href']
            ulist1.append([title,link])
        except:
            continue
    return ulist1


def getdownUrl(downurl):
    res = requests.get(downurl,headers=headers,proxies=proxies,timeout=30)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text,'html.parser')
    rxs = soup.find_all('div',class_='cta-button-container__item')
    link = rxs[0].select('a')[0]['href']
    totallink = 'https://link.springer.com' + link
    return totallink

if __name__ == "__main__":
    url = 'https://www.reddit.com/r/FreeEBOOKS/comments/g34xi5/408_free_ebooks_from_springer/'
    ulist1 = []
    ulist1 = getUrl(url)
    downlist = []
    for i in range(len(ulist1)):
        downurl = ulist1[i][1]
        try:
            lik = getdownUrl(downurl)
            #print(ulist[i][0])
            print(lik)
        except:
            continue
