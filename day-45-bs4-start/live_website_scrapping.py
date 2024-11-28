from bs4 import BeautifulSoup
import requests

WEBSITE = 'https://appbrewery.github.io/news.ycombinator.com/'

content = requests.get(WEBSITE)
soup = BeautifulSoup(content.text, 'html.parser')

all_story_links = soup.find_all(class_='storylink')
all_scores = soup.find_all(class_='score')

links_with_upvote = [(story_link.get_text(), story_link.get('href'), int(score.get_text().split()[0]))
                     for story_link, score
                     in zip(all_story_links, all_scores)]

print(links_with_upvote)

# getting link with the max upvote
print(max(links_with_upvote, key=lambda link: link[2]))

# sorting list by upvote decreasing
links_with_upvote.sort(key=lambda link: link[2], reverse=True)

print(links_with_upvote)

# checking if the first item of sorted list is the same as the link with the max upvote gotten by other function
print(links_with_upvote[0])
