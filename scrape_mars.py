from bs4 import BeautifulSoup as bs
from splinter import Browser
import requests
import pandas as pd
import time

def scrape():
    
    #NEWS
    nasaUrl = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    html = requests.get(nasaUrl)
    
    soup = bs(html.text, 'lxml')
   
    news_title = soup.find_all(class_='content_title')[0].text
    news_p = soup.find_all(class_='rollover_description_inner')[0].text
    
    #Featured Image
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False, wait_time = 5)
    
    marsUrl = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(marsUrl)  
    time.sleep(5)
    browser.click_link_by_partial_text('FULL IMAGE')    
    time.sleep(5)
    browser.click_link_by_partial_text('more info') 
    browser.click_link_by_partial_href('/jpeg')
    featuredImageUrl = browser.find_by_css('img')['src']
    
    #Mars Weather    
    twitterUrl = 'https://twitter.com/marswxreport?lang=en'
    html = requests.get(twitterUrl)
    
    soup = bs(html.text, 'lxml')
    
    marsWeather = soup.find_all(class_='TweetTextSize')[0].text
    
    #Mars Facts
    marsFactsUrl = 'https://space-facts.com/mars/'
    
    df = pd.read_html(marsFactsUrl)[0]
    
    #Hemispheres
    marsHemispheresUrl = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(marsHemispheresUrl)
    
    hemiList = []
    
    marsHemispheresUrl = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(marsHemispheresUrl)
    browser.click_link_by_partial_text('Cerberus Hemisphere')
    img_url = browser.find_by_css('img[class = wide-image]')['src']
    title = browser.find_by_css('h2[class = title]').text
    hemiList.append(dict({'title': title, 'img_url': img_url}))
    
    marsHemispheresUrl = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(marsHemispheresUrl)
    browser.click_link_by_partial_text('Schiaparelli Hemisphere')
    img_url = browser.find_by_css('img[class = wide-image]')['src']
    title = browser.find_by_css('h2[class = title]').text
    hemiList.append(dict({'title': title, 'img_url': img_url}))
    
    marsHemispheresUrl = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(marsHemispheresUrl)
    browser.click_link_by_partial_text('Syrtis Major Hemisphere')
    img_url = browser.find_by_css('img[class = wide-image]')['src']
    title = browser.find_by_css('h2[class = title]').text
    hemiList.append(dict({'title': title, 'img_url': img_url}))
    
    marsHemispheresUrl = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(marsHemispheresUrl)
    browser.click_link_by_partial_text('Valles Marineris Hemisphere')
    img_url = browser.find_by_css('img[class = wide-image]')['src']
    title = browser.find_by_css('h2[class = title]').text
    hemiList.append(dict({'title': title, 'img_url': img_url}))

    scrapedDict = {'news_title': news_title, 'news_p': news_p, 'featured_image':featuredImageUrl, 'weather': marsWeather, 'facts': df, 'hemispheres': hemiList}

    return scrapedDict



