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

    pre_facts = pd.read_html("https://space-facts.com/mars/")[1]
    pre_facts.columns = ['Mars - Earth Comparison','Mars','Earth']
    pre_facts.set_index("Mars - Earth Comparison", inplace = True)
    mars_facts = pre_facts.to_html()
    print(pre_facts)

    #connet to cerberus hemispheres
    url_cerberus = "https://marshemispheres.com/cerberus.html"
    browser.visit(url_cerberus)
 
    #start to scrap the name of cerberus
    html = browser.html
    soup = bs(html, "html.parser")
    cerberus = soup.find("h2", class_="title").get_text()
    
    #start to scrap the html of cerberus
    content = browser.find_link_by_text("Sample").first
    cerberus_link = content['href']
    
    cerberus_hem = {"title": cerberus, "img_url": cerberus_link}

    #connet to schiaparelli hemispheres
    url_schiaparelli = "https://marshemispheres.com/schiaparelli.html"
    browser.visit(url_schiaparelli)

    #start to scrap the name of schiaparelli
    html = browser.html
    soup = bs(html, "html.parser")
    schiaparelli = soup.find("h2", class_="title").get_text()
    
    #start to scrap the html of schiaparelli
    content = browser.find_link_by_text("Sample").first
    schiaparelli_link = content['href']
    
    schiaparelli_hem = {"title": schiaparelli, "img_url": schiaparelli_link}

    #connet to syrtis major hemispheres
    url_syrtis = "https://marshemispheres.com/syrtis.html"
    browser.visit(url_syrtis)

    #start to scrap the name of syrtis major
    html = browser.html
    soup = bs(html, "html.parser")
    syrtis = soup.find("h2", class_="title").get_text()
    
    #start to scrap the html of syrtis major
    content = browser.find_link_by_text("Sample").first
    syrtis_link = content['href']
    
    syrtis_hem = {"title": syrtis, "img_url": syrtis_link}

    #connet to syrtis valles hemispheres
    url_valles = "https://marshemispheres.com/valles.html"
    browser.visit(url_valles)

    #start to scrap the name of valles major
    html = browser.html
    soup = bs(html, "html.parser")
    valles = soup.find("h2", class_="title").get_text()

    #start to scrap the html of valles
    content = browser.find_link_by_text("Sample").first
    valles_link = content['href']

    valles_hem = {"title": valles, "img_url": valles_link}
    hemisphere_image_urls = []
    hemisphere_image_urls.append(cerberus_hem)
    hemisphere_image_urls.append(schiaparelli_hem)
    hemisphere_image_urls.append(syrtis_hem)
    hemisphere_image_urls.append(valles_hem)


    
    listing['first_title'] = first_title
    listing['first_para'] = first_para
    listing['image_url'] = featured_image_url
    listing['table'] = mars_facts
    listing['hemisphere_image'] = hemisphere_image_urls
    
    browser.quit()
    
    return listing
    

