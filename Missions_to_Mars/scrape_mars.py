#Dependencies and Setup

from splinter import Browser
from bs4 import BeautifulSoup as bs
from  webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

#Set executable path & initialize chrome browser

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


#for the scrape button on the main page

def scrape_all():
    
    listing = {}

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

    #link to mars space images website
    url = "https://spaceimages-mars.com/"
    browser.visit(url)

    #start to scrap the page of space images
    html = browser.html
    soup = bs(html, "html.parser")
    pic_content = soup.select_one("div",class_="thmbgroup")

    #scrape the href of the page
    image_url = pic_content.find_all("a",class_="fancybox-thumbs")[0]['href']

    #store a full html link for picture
    featured_image_url =f'https://spaceimages-mars.com/{image_url}'

    mars_facts = pd.read_html("table.html")

    #connet to Mars Facts
    url = "https://marshemispheres.com"
    browser.visit(url)

    #start to scrap the table from Mars Facts
    html = browser.html
    soup = bs(html, "html.parser")
    hemis = soup.find("div", class_="collapsible results")

    #get a list of how many pictures contains inside
    categories = hemis.find_all('div', class_= 'item') 

    hemisphere_image_urls = []

    for category in categories:
        hemisphere = {}
    
        #find image url and title and put into dictionary
        image_src = category.find("img",class_="thumb")['src']
        hemisphere['title'] = category.find('h3').get_text()
        hemisphere['img_url'] = f'https://marshemispheres.com/{image_src}'
    
        #put the hemisphere into a list
        hemisphere_image_urls.append(hemisphere)
    
    listing['first_title'] = first_title
    listing['first_para'] = first_para
    listing['image_url'] = featured_image_url
    listing['table'] = mars_facts
    listing['hemisphere_image'] = hemisphere_image_urls

    return listing

