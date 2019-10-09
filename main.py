import reqests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.com/EVGA-GeForce-Gaming-GDDR5X-Technology/dp/B06Y13N2B6/ref=sr_1_3?keywords=gtx+1080+ti&qid=1564329476&s=gateway&sr=8-3'

headers = {"User Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36
'}

def checkPrice():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id = "productTitle").get_text()
    price = soup.find(id = "priceblock_ourprice").get_text()
    convertedPrice = float(price[0:5])

    if(convertedPrice < 1.700)
        send_mail()

    print(convertedPrice)
    print(title.strip())

def send_mail():
    myServer = smtplib.SMTP('smtp.gmail.com', 587)
    myServer.ehlo()
    myServer.starttls()
    myServer.ehlo()

    myServer.login('afnan.latif01@gmail.com', #user password)
    subject = "The price has fallen"
    body = "Your item: https://www.amazon.com/EVGA-GeForce-Gaming-GDDR5X-Technology/dp/B06Y13N2B6/ref=sr_1_3?keywords=gtx+1080+ti&qid=1564329476&s=gateway&sr=8-3"

    msg = f"Subject: {subject}\n\n{body}"

    server.send_mail(afnan.latif01@gmail.com, afnan.latif01@gmail.com, msg)

    print("sent")

    myServer.quit()
