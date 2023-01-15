import requests
from bs4 import BeautifulSoup
import smtplib

user_agent_header = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0"
accept_language_header = "en-US,en;q=0.5"

headers = {
        "User-Agent": user_agent_header,
        "Accept-Language": accept_language_header,
        }
amazon_url= "https://www.amazon.com/gp/product/B09G62S6ZZ/ref=ewc_pr_img_1?smid=A3L8G1TGO8S0OG&th=1"

response = requests.get(amazon_url, headers=headers)

web_page=response.text
soup=BeautifulSoup(web_page, "html.parser")

whole_price = soup.find(name="span", class_="a-price-whole").getText()

fraction_price = soup.find(name="span", class_="a-price-fraction").getText()

current_price=float(whole_price+fraction_price)

target_price = 28.40

if current_price < target_price:
    my_email="BrandonHang.Business@gmail.com"
    my_password=""

    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(
            from_addr=my_email,
            to_addrs="brandonhang34@outlook.com",
            msg=f"Subject:Amazon Price\n\nThe price has reached below the target price (${target_price}) for this item:{amazon_url}")
    connection.close()
            
