import requests
from bs4 import BeautifulSoup

music_date = input("Which year do you want to travel to? Type the date in YYYY-MM-DD format: ")
# music_date = "1994-12-12"
response = requests.get(f"https://www.billboard.com/charts/hot-100/{music_date}")
response_text = response.text
# print(response_text)

soup = BeautifulSoup(response_text, "html.parser")

# ACCESSING TITLES
title_soup = soup.find_all(name="h3", id="title-of-a-story", class_="c-title")
song_titles = [song.getText().strip() for song in title_soup]
song_titles = [title for title in song_titles if title != "Songwriter(s):" if title != "Producer(s):" if title != "Imprint/Promotion Label:"]
song_titles = song_titles[3::]
print(song_titles)

# ACCESSING ARTISTS
artist_soup = soup.find_all(name="span", class_="c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only")
song_artists = [artist.getText().strip() for artist in artist_soup]
number_one_artist = soup.find(name="span", class_="c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only u-font-size-20@tablet").getText().strip()
song_artists.insert(0, number_one_artist)
print(song_artists)

