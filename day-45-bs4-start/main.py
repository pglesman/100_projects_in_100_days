from bs4 import BeautifulSoup

with open('website.html') as file:
    content = file.read()

soup = BeautifulSoup(content, 'html.parser')

print(soup.title)
print(soup.title.name)
print(soup.title.string)

# print the whole page with nice indentation
# print(soup.prettify())

# print first founded item on the page
print(soup.li)
print(soup.a)

# get all anchor tags (links to other pages
all_anchor_tags = soup.find_all(name='a')

# all links on the page
for tag in all_anchor_tags:
    print(tag.get('href'))

print(soup.find(id='name').string)
print(soup.find(class_='heading').string)

# using a CSS selector -> find a link that is only in paragraph, you can use it also in CSS styling
company_url = soup.select_one(selector='p a')
print(company_url.get('href'))
