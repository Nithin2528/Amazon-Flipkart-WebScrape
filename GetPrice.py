import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent":"Mozilla/5.0(X11;Linux x86_64)AppleWebKit/537.36(KHTML,like Gecko)Chrome/51.0.2704.103 Safari/537.36"
}
search = input("Paste the product link: ")
respone = requests.get(search , headers = headers)
soup = BeautifulSoup(respone.content,'html.parser')


def check_price():
    title = soup.find(id = "productTitle").get_text()
    price = soup.find(id = "priceblock_ourprice").get_text().strip()
    print("Product name & Specs : " , title.strip())
    print("Product Cost: " , price)


check_price()
    
