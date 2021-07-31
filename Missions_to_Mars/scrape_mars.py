#Dependencies and Setup

from splinter import Browser
from bs4 import BeautifulSoup as bs
from  webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

#Set executable path & initialize chrome browser

executable_path = {'executable_path': ChromeDriverManager().install()}
broser = Browser('chrome', **executable_path, headless=False)

#Mars News Site
#Scraping from that
def mars_news(browser):

    #use chrome to visit mars news site
    url = 'https://redplanetscience.com'
    browser.visit(url)

    #start to scrap the page of mars news
    html = browser.html
    soup = bs(html, "html.parser")
    title_content = soup.select_one("div", class_ ="col-md-12")

    #scrape the first title
    first_title = title_content.find_all("div", class_="content_title")[0].get_text()

    #scrape the first subtitle
    first_para = title_content.find_all("div", class_='artivle_teaser_body')[0].get_text()

    return first_title, first_para


#Mars Space Images
#Scraping from browser

def featured_image(browser):
    
