from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

# print(soup.title)

number1=soup.find_all(name="a", class_="storylink")
# print(number1)


article_texts=[]
articles_links=[]

a=soup.select("tr td table td span a")
# print(a[9].getText())

article_link = a[9].get("href")
# print(article_link)

votes=soup.find_all(name="span", class_="score")
# print(votes)

for article_tag in a[9:]:
    article_text=article_tag.getText()
    article_texts.append(article_text)
    article_link = article_tag.get("href")
    articles_links.append(article_link)
print(article_texts)
# with open("website.html") as website:
#     content=website.read()

# soup = BeautifulSoup(content, "html.parser")
# # print(soup.title)

# # print(soup.title.string)

# # print(soup.p)

# all_anchor_tags=soup.find_all(name="a")
# print(all_anchor_tags)

# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)

# section_heading=soup.find(name="h3", class_="heading")
# print(section_heading)
