# write a web scraper that will scrape the following website: 
# This is a web scraping python project where the html is collected from a website. The Html is then used to create an Html document. All links in the main website provided are also scraped and html files created with their page titles as the names
import requests
from bs4 import BeautifulSoup
# Making a GET request
def scrapeWebsite(url):
  try:
      r = requests.get(url)
      if(r.status_code != 200):
          raise Exception("Error: Status code is not 200")
      else:
          print("Success: Status code is 200")
          return r.content
  except:
      return "Error: Status code is not 200"
  
# function to save html content to a html file
def saveHTML(htmlContent, fileName):
  with open(fileName+'.html', 'w', encoding='utf-8') as f:
    f.write(f'''{htmlContent}''')
    f.close()

websiteSoup = BeautifulSoup(scrapeWebsite('https://www.geeksforgeeks.org/python-programming-language/'), "html.parser")
saveHTML(websiteSoup.prettify(), websiteSoup.title.string)
aTags = websiteSoup.find_all('a', href=True)
amountOfLinks = len(aTags)
print(f"There are {amountOfLinks} links on this page")
# for tag in aTags:
#     print(tag.get('href'))

# # check status code for response received
# # success code - 200
# print(type(r))
 
# print content of request
# print(r.content)