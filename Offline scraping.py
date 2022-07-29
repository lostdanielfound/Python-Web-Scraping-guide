from bs4 import BeautifulSoup

with open('website.html') as site:
    soup = BeautifulSoup(site, 'lxml')

# Experimenting with how to use the attributes
siteTitle = soup.title
firstDiv = soup.find('div')
divFooter = soup.find('div', class_ = 'footer')
footerText = divFooter.p.text

# Getting the article headline and summaries from a page
allArticles = soup.find_all('div', class_ = 'article') # dictionary

# printing each article head
for head in allArticles:
    print(head.h2.a.text)

for summary in allArticles:
    print(summary.p.text)
