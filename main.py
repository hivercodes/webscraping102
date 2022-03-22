from bs4 import BeautifulSoup
import requests

website_request = requests.get(url="https://www.empireonline.com/movies/features/best-movies-2")
data = website_request.text

soup = BeautifulSoup(data, "html.parser")

article = soup.article.find_all("div", {"class": "article-content"})

data = article[0]

print(data)