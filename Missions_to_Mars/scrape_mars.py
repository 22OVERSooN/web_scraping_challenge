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
    

    #scrape the first title
    first_title = soup.find_all("div", class_="content_title")[0].get_text()

    #scrape the first subtitle
    first_para = soup.find_all("div", class_='article_teaser_body')[0].get_text()

    #link to mars space images website
    url_img = "https://spaceimages-mars.com/"
    browser.visit(url_img)

    #start to scrap the page of space images
    html = browser.html
    soup = bs(html, "html.parser")
    pic_content = soup.select_one("div",class_="thmbgroup")

    #scrape the href of the page
    image_url = pic_content.find_all("a",class_="fancybox-thumbs")[0]['href']

    #store a full html link for picture
    featured_image_url =f'https://spaceimages-mars.com/{image_url}'

    #connect to Mars Facts
    #Scraping from that browser

    url_facts = "https://galaxyfacts-mars.com/"
    browser.visit(url_facts)

    #start to scrap the table from Mars Facts
    html = browser.html
    soup = bs(html, "html.parser")
    table_content = soup.select_one("table", class_="table table-striped")

    #create the list for table
    index = []
    mars_list = []
    earth_list = []

    categories = table_content.find_all('tr')

    for category in categories:
        index.append(category.find('th').get_text())
        mars_list.append(category.find_all('td')[0].get_text())
        earth_list.append(category.find_all('td')[1].get_text())

    #put the table into panda and do some adjustment
    df = pd.DataFrame(list(zip(index,mars_list,earth_list)))
    df = df.set_index(0)
    df.columns = ['Mars', 'Earth']
    df.index.name = 'Mars-Earth Comparison'
    df = df.iloc[1:,:]
    df.loc['Temperature:','Earth'] = '-88 to 58°C'

    #create the mars_facts html code for table
    mars_facts = df.to_html()

    #connect to Mars Hemisphere
    url_hemi = "https://marshemispheres.com"
    browser.visit(url_hemi)

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

