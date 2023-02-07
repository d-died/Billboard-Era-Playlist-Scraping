import requests
from bs4 import BeautifulSoup

# music_date = input("Which year do you want to travel to? Type the date in YYYY-MM-DD format: ")
music_date = "1994-12-19"
response = requests.get(f"https://www.billboard.com/charts/hot-100/{music_date}")
response_text = response.text

soup = BeautifulSoup(response_text, "html.parser")
top_100_songs = soup.find_all(name="div", class_="o-chart-results-list-row-container")


# for song in top_100_songs:
#     song_titles =
