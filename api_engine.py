import requests
from bs4 import BeautifulSoup as BS


def getStock(isbn):
    url = 'http://www.kyobobook.co.kr/prom/2013/general/StoreStockTable.jsp?barcode=' + isbn + '&ejkgb=KOR'
    res = requests.get(url)
    soup = BS(res.text, 'html.parser')
    # 비어있는 태그들 삭제
    [x.decompose() for x in soup.findAll(lambda tag: (not tag.contents or len(tag.get_text(strip=True)) <= 0))]
    store = soup.select('th')
    num = soup.select('a')
    stock = {}
    for i, j in zip(store, num):
        i = i.text
        i = i.strip()
        if i == '':
            pass
        else:
            stock[i] = j.text
    return stock


def bookInfo(title):
    clientId = "BsGqKYMK02FYfiAaMGCh"
    clientSecret = "FcO6DvI5Yb"
    url = "https://openapi.naver.com/v1/search/book?query=" + title + "&display=5&sort=count"
    headers = {"X-Naver-Client-Id": clientId, "X-Naver-Client-Secret": clientSecret}
    res = requests.get(url, headers=headers)
    search = res.json()
    book = search['items']
    for i in book:
        for j in i:
            i[j] = i[j].replace('<b>', '').replace('</b>', '')
        i['isbn'] = i['isbn'][11:]
    return book
