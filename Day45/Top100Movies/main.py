from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
web_page=response.text

soup = BeautifulSoup(web_page, "html.parser")

movie_titles=soup.find_all(name="h3", class_="title")


print(movie_titles)

titles=[]

for movies in movie_titles:
    titles.append(movies.getText())

with open("movies.txt", "a") as file:
    for i in reversed(range(len(titles))):
        file.write(f"{titles[i]}\n")
