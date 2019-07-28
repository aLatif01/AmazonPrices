import reqests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.com/EVGA-GeForce-Gaming-GDDR5X-Technology/dp/B06Y13N2B6/ref=sr_1_3?keywords=gtx+1080+ti&qid=1564329476&s=gateway&sr=8-3'

headers = {"User Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36
'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')
