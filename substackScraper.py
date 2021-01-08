#!/usr/bin/env python3
# substackScraper.py - Web Scraper for Substack articles 

import requests, pyperclip, bs4, sys
# get url
if len(sys.argv) > 1 :
    # from command line
    url = sys.argv[1]
else: 
    # from clipboard
    url = pyperclip.paste()
# download the html source file from url
res = requests.get(url)
# check connection is succesful
res.raise_for_status()
# get text from respond object
soup = bs4.BeautifulSoup(res.text, 'html.parser') 
# use beautifulsoup object method to parse out the main paragraph 
elem = soup.select('.post')
print(elem[0].getText())
# TODO retain the formatting of the paragraph

# TODO save paragraph in a file on hard drive

