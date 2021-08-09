import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.walmart.com/ip/Sony-PlayStation-5-Video-Game-Console/994712501'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36,'}
headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64)', 'Cache-Control': 'no-cache', "Pragma": "no-cache"}

def check_stock():

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')


    title = soup.find("h1", class_="prod-ProductTitle").get_text()
    stock = soup.find(id="blitzitem-container").get_text()
    converted_stock_string = stock
    converted_stock = (converted_stock_string.replace(',',''))

 

#   print(converted_stock_string)
#   print(converted_stock)
    print(title)
    print(stock)

  #  print (soup)

    if(converted_stock != "This item is out of stock"):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(
 #      'username'
        ,
 #      'Password Here'
                )

    subject = 'PS5 in Stock at Walmart!'
    body = 'Check the walmart link https://www.walmart.com/ip/Sony-PlayStation-5-Video-Game-Console/994712501'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
#        'email from here',
#        'email send to here',
        msg

    )
    print('Email Sent out')

    server.quit()

check_stock()
while True:
    check_stock()
    #should check every hour
    time.sleep(60 * 60)
