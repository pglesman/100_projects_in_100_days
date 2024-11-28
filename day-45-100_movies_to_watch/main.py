import requests
from bs4 import BeautifulSoup
import re

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

content = requests.get(URL)
soup = BeautifulSoup(content.text, 'lxml')

titles_list_tag = soup.find_all(name='h3', class_='title')
titles_list = [title.get_text().split(maxsplit=1) for title in titles_list_tag]

# sort a list by a key that was a position of a film but in the string with title and also with ')' and ':'
titles_list.sort(key=lambda title: int(re.split(r'[):]', title[0])[0]))
# print(titles_list)

titles_sorted = [' '.join(title) for title in titles_list]
# print(titles_sorted)

with open('movies.txt', mode='w', encoding="utf-8") as file:
    file.writelines(line + '\n' for line in titles_sorted)
    print("File was created!")
