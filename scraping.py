


#import dependencies for Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

#Set the executable path
executable_path = {'executable_path': ChromeDriverManager().install()}

#set up the Browser url for scrapping
browser = Browser('chrome', **executable_path, headless=False)

#assign the URL and instruct the browser to visit it
#visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)

#operational deal for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)
#what we are doing here is 1. searching for elements with a specific comination of tag (div and sttribute list_text)
# and 2. we are telling the browser to wait one second before searching for components

# Set up the html parser
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')
#slide_elem looks for the <div /> tag and its descendent
#this element holds all other elements in it
# the . is used for selecting classes (aka list_text here in this example)
# css works from right to left (such as returning the last item instead of the first)
# because of this, when using select_one, the first matching element returned will be a <li /> element with a class of slide

#assign the title and summary text to variables
#begin our scraping
slide_elem.find('div', class_='content_title')
#look for specific data


# use the parent element to find the first 'a' tag and save it as 'news_title'
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title
# get text removes the html code and only keeps the text in between
#.find() is used when we want only the first class and attribute we specified
#.find_all() is used when we want to retrieve all of the tags and attributes


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images

# set up the url 
#Visit the space image site
url = 'https://spaceimages-mars.com'
browser.visit(url)


#find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# set up the html.parser to full parse the image so we can scrape the full size
html = browser.html
img_soup = soup(html, 'html.parser')


# find the relative image URL 
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel
# an img tag is nested within the HTML, so we have included it
#.get('src') pulls the link to the image


# use the base URL to create an absolute URL
img_url = f'https://speaceimages-mars.com{img_url_rel}'
img_url


# ### Getting the table data from mars facts

#create a new datafram from the HTML table
df = pd.read_html('https://galaxyfacts-mars.com')[0]
#assign columns to the datafram for additional clarity
df.columns=['description', 'Mars', 'Earth']
# turn the description column into the dataframes index
#inplace=true means that the updated index will remain in place without having to reassign the df to a new variable
df.set_index('description', inplace=True)
df


# use pandas to revert the dataframe back into HTML usinng the .to_html() function
df.to_html()
#this creates a table element with a lot of nested elements inside


# end the automated browsing session
browser.quit()



