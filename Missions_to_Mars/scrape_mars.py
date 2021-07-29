from splinter import Browser
from bs4 import BeautifulSoup as bs
from  webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import datatime as dt

executable_path = {'executable_path': ChromeDriverManager().install()}
broser = Browser('chrome', **executable_path, headless=False)

def scrape_title()：

    url = 'https://redplanetscience.com'
    browser.visit(url)




    browser.