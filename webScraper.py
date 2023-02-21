# write a web scraper that will scrape the following website: 
# This is a web scraping python project where the html is collected from a website. The Html is then used to create an Html document. All links in the main website provided are also scraped and html files created with their page titles as the names

import six
from google.cloud import translate_v2 as translate
from google.oauth2 import service_account
import os
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./HiddenData/driven-net-292012-e48cd2296ff5.json"
credentials = service_account.Credentials.from_service_account_file("./HiddenData/driven-net-292012-e48cd2296ff5.json")
translator = translate.Client(credentials=credentials)


def translate_text(target, text):
    """Translates text into the target language.

    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """

    translate_client = translate.Client()

    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(text, target_language=target)

    return result['translatedText']
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
# function to translate html content to hindi
def translateHTML(htmlContent):
    # Extract the text content from the HTML
    textContent = htmlContent 
    BeautifulSoup(htmlContent, 'html.parser').get_text()

    # Translate the text content to Hindi
    translatedText = translate_text('hi', textContent)

    # Insert the translated text back into the HTML
    translatedHTML = htmlContent.replace(textContent, translatedText)

    return translatedHTML


# function to save html content to a html file
def saveHTML(htmlContent, fileName):
  directory = 'html'
  if not os.path.exists(directory):
   os.makedirs(directory)
  filePath = os.path.join(directory, fileName + '.html')
  with open(filePath, 'w', encoding='utf-8') as f:
    f.write(f'''{htmlContent}''')
    
# url = input("Enter the URL of the website to scrape: ")
websiteSoup =  BeautifulSoup(scrapeWebsite('https://www.classcentral.com/'), "html.parser")
if websiteSoup.title.string:
  titleTranslated = translate_text('hi', websiteSoup.title.string)
  saveHTML(websiteSoup.prettify(), titleTranslated)
else:
  saveHTML(websiteSoup.prettify(), "NoTitle")
aTags = websiteSoup.find_all('a', href=True)
# amountOfLinks = len(aTags)
# print(f"There are {amountOfLinks} links on this page")
count = 0
for tag in aTags:
  if(tag.get('href').startswith('https://')):
    count = count + 1
    print(tag.get('href'))
    data = BeautifulSoup(scrapeWebsite(tag.get('href')), "html.parser")
    pTags = data.find_all('p')
    if data.title.string:
      translatedTitle = translate_text('hi', data.title.string)
      
      saveHTML(data.prettify(),translatedTitle)
    else:
      saveHTML(data.prettify(), "NoTitle")
print(count)
# # check status code for response received
# # success code - 200
# print(type(r))
 
# print content of request
# print(r.content)