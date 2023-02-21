# write a web scraper that will scrape the following website: 
# This is a web scraping python project where the html is collected from a website. The Html is then used to create an Html document. All links in the main website provided are also scraped and html files created with their page titles as the names
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
# Making a GET request
def scrapeWebsite(url):
  headers = {
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
  'Accept-Encoding': 'none',
  'Accept-Language': 'en-US,en;q=0.8',
  'Connection': 'keep-alive',
  'refere': url,
  'cookie': """your cookie value ( you can get that from your web page) """
}
  try:
      req = Request(url, headers=headers)
      # get the status code of the req
      res = urlopen(req)
      print(res.status)
      if(res.status == 200):
          return res.read()   
      else:
          raise Exception("Error: Status code is not 200")
  except:
      return "Error: Status code is not 200"
  
# function to save html content to a html file
def saveHTML(htmlContent, fileName):
  with open(fileName+'.html', 'w', encoding='utf-8') as f:
    f.write(f'''{htmlContent}''')
    f.close()
#
websiteSoup =  BeautifulSoup(scrapeWebsite('https://www.classcentral.com'), "html.parser")
if websiteSoup.title.string:
  saveHTML(websiteSoup.prettify(), websiteSoup.title.string)
else:
  saveHTML(websiteSoup.prettify(), "NoTitle")
aTags = websiteSoup.find_all('a', href=True)
# amountOfLinks = len(aTags)
# print(f"There are {amountOfLinks} links on this page")
count = 0
for tag in aTags:
  if(tag.get('href').startswith('https://www.')):
    count = count + 1
    print(tag.get('href'))
    data = BeautifulSoup(scrapeWebsite(tag.get('href')), "html.parser")
    if data.title.string:
      saveHTML(data.prettify(), data.title.string)
    else:
      saveHTML(data.prettify(), "NoTitle")
print(count)
# # check status code for response received
# # success code - 200
# print(type(r))
 
# print content of request
# print(r.content)