import requests
from bs4 import BeautifulSoup
import smtplib
import time
# check website to make sure it is active since it changes
ps5_Site = 'https://www.walmart.com/ip/Sony-PlayStation-5-Video-Game-Console/363472942'
URL = ps5_Site


headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36,'}
headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64)', 'Cache-Control': 'no-cache', "Pragma": "no-cache"}

def check_stock():

    page = requests.get(URL, headers=headers)
    instock = ""
    soup = BeautifulSoup(page.content, 'html.parser')

    global price
    title = soup.find("span", itemprop="name").get_text()
    price = soup.find("span", itemprop="price").get_text()
    try:
        stock = soup.find(id="blitzitem-container").get_text()
        converted_stock_string = stock
        converted_stock = (converted_stock_string.replace(',',''))
        print (stock)
    except AttributeError:
        instock = "In Stock"
        print ("In Stock")

 

#   print(converted_stock_string)
#   print(converted_stock)
    print(title)
    print(price)
    

  #  print (soup)
    

    if(instock == "In Stock" and float(price[1:]) < 600 ):
        send_mail()    

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(
   #     'username here'
        , 
   #     'password here'
    )

    subject = 'PS5 in Stock at Walmart for ' + str(price) + '!'
    body = 'Check the walmart link ' + str(ps5_Site)

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'avillalobos.code@gmail.com',
        'angel_villalobos5@yahoo.com',
        msg

    )
    print('Email Sent out')

    server.quit()


while True:
    check_stock()
    #check every hour
    time.sleep(60 * 60)
