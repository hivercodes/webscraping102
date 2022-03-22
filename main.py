from bs4 import BeautifulSoup
import requests

website_request = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
data = website_request.text

soup = BeautifulSoup(data, "html.parser")

all_movies = []

data = soup.find_all(name="h3", class_="title")

for d in data:
    all_movies.append(d.text)


print(all_movies[::-1])

with open("movie.list", "a") as movies:
    for item in all_movies[::-1]:
        movies.write(f"{item}\n")