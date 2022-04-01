#Mobility Trends Reports Code

import requests
from bs4 import BeautifulSoup
url = "https://covid19.apple.com/mobility"
r = requests.get(url)
htmlContent = r.content
print(htmlContent)
soup = BeautifulSoup(htmlContent, 'html.parser')
print(soup.prettify)

markup = "<p><!-- this is a comment --></p>"
soup2 = BeautifulSoup(markup)
print(type(soup2.p.string))

title = soup.title
print(type(soup))
print(type(title))
print(type(title.string))
paras = soup.find_all('p')
print(paras)
anchors = soup.find_all('a')
all_links = set()
for link in anchors:
    if(link.get('href') != '#'):
        linkText =  "https://covid19.apple.com/mobility" +link.get('href')
        all_links.add(link)
        print(linkText)
print(anchors)
print(soup.find('p'))
print(soup.find('p')['class'])
print(soup.find_all("p", class_="lead"))

#Get the text from the tags/soup
print(soup.find('p').get_text())
print(soup.get_text())

#Google Mobility Index

import requests
from bs4 import BeautifulSoup
url = "https://www.google.com/covid19/mobility/"
r = requests.get(url)
htmlContent = r.content
print(htmlContent)
soup = BeautifulSoup(htmlContent, 'html.parser')
print(soup.prettify)

markup = "<p><!-- this is a comment --></p>"
soup2 = BeautifulSoup(markup)
print(type(soup2.p.string))

title = soup.title
print(type(soup))
print(type(title))
print(type(title.string))
paras = soup.find_all('p')
print(paras)
anchors = soup.find_all('a')
all_links = set()
for link in anchors:
    if(link.get('href') != '#'):
        linkText =  "https://www.google.com/covid19/mobility/" +link.get('href')
        all_links.add(link)
        print(linkText)
print(anchors)
print(soup.find('p'))
print(soup.find('p')['class'])
print(soup.find_all("p", class_="lead"))

#Get the text from the tags/soup
print(soup.find('p').get_text())
print(soup.get_text())

#Git Commits

import requests
from bs4 import BeautifulSoup
url = "https://docs.github.com/en/rest/reference/repos#commits"
r = requests.get(url)
htmlContent = r.content
print(htmlContent)
soup = BeautifulSoup(htmlContent, 'html.parser')
print(soup.prettify)

markup = "<p><!-- this is a comment --></p>"
soup2 = BeautifulSoup(markup)
print(type(soup2.p.string))

title = soup.title
print(type(soup))
print(type(title))
print(type(title.string))
paras = soup.find_all('p')
print(paras)
anchors = soup.find_all('a')
all_links = set()
for link in anchors:
    if(link.get('href') != '#'):
        linkText =  "https://docs.github.com/en/rest/reference/repos#commits" +link.get('href')
        all_links.add(link)
        print(linkText)
print(anchors)
print(soup.find('p'))
print(soup.find('p')['class'])
print(soup.find_all("p", class_="lead"))

#Get the text from the tags/soup
print(soup.find('p').get_text())
print(soup.get_text())

#Google Earth Engine API

import requests
from bs4 import BeautifulSoup
url =" https://developers.google.com/earth-engine"
r = requests.get(url)
htmlContent = r.content
print(htmlContent)
soup = BeautifulSoup(htmlContent, 'html.parser')
print(soup.prettify)

markup = "<p><!-- this is a comment --></p>"
soup2 = BeautifulSoup(markup)
print(type(soup2.p.string))

title = soup.title
print(type(soup))
print(type(title))
print(type(title.string))
paras = soup.find_all('p')
print(paras)
anchors = soup.find_all('a')
all_links = set()
for link in anchors:
    if(link.get('href') != '#'):
        linkText =  "https://developers.google.com/earth-engine" +link.get('href')
        all_links.add(link)
        print(linkText)
print(anchors)
print(soup.find('p'))
print(soup.find('p')['class'])
print(soup.find_all("p", class_="lead"))

#Get the text from the tags/soup
print(soup.find('p').get_text())
print(soup.get_text())

#City of Sunnyvale Public Procurement

import requests
from bs4 import BeautifulSoup
url ="https://www.demandstar.com/app/agencies/california/city-of-sunnyvale/procurement-opportunities/e9a860f4-8f17-43af-aae7-e5dc8389f36e/"
r = requests.get(url)
htmlContent = r.content
print(htmlContent)
soup = BeautifulSoup(htmlContent, 'html.parser')
print(soup.prettify)

markup = "<p><!-- this is a comment --></p>"
soup2 = BeautifulSoup(markup)
print(type(soup2.p.string))

title = soup.title
print(type(soup))
print(type(title))
print(type(title.string))
paras = soup.find_all('p')
print(paras)
anchors = soup.find_all('a')
all_links = set()
for link in anchors:
    if(link.get('href') != '#'):
        linkText =  "https://www.demandstar.com/app/agencies/california/city-of-sunnyvale/procurement-opportunities/e9a860f4-8f17-43af-aae7-e5dc8389f36e/" +link.get('href')
        all_links.add(link)
        print(linkText)
print(anchors)
print(soup.find('p'))
print(soup.find('p')['class'])
print(soup.find_all("p", class_="lead"))

#Get the text from the tags/soup
print(soup.find('p').get_text())

#UK Cabinet Contracts

import requests
from bs4 import BeautifulSoup
url ="https://www.gov.uk/contracts-finder"
r = requests.get(url)
htmlContent = r.content
print(htmlContent)
soup = BeautifulSoup(htmlContent, 'html.parser')
print(soup.prettify)

markup = "<p><!-- this is a comment --></p>"
soup2 = BeautifulSoup(markup)
print(type(soup2.p.string))

title = soup.title
print(type(soup))
print(type(title))
print(type(title.string))
paras = soup.find_all('p')
print(paras)
anchors = soup.find_all('a')
all_links = set()
for link in anchors:
    if(link.get('href') != '#'):
        linkText =  "https://www.gov.uk/contracts-finder" +link.get('href')
        all_links.add(link)
        print(linkText)
print(anchors)
print(soup.find('p'))
print(soup.find('p')['class'])
print(soup.find_all("p", class_="lead"))

#Get the text from the tags/soup
print(soup.find('p').get_text())
print(soup.get_text())
print(soup.get_text())


