#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
This script gets all the quotes from danstonchat, the french quote website.
"""

from bs4 import BeautifulSoup
import urllib2
import re

# Main variables
elements = []
list_links = []
liste_quote = []


class DTCScrapper(object):
    """Class to get the quotes form danstonchat.fr"""

    # I get the web page with the quote.
    def get_web_page_content(self,url):
        web_page_content = ""
        try:
            web_page_content = urllib2.urlopen(url)
        except:
            print("Error, I could not the content from the page " + str(url))
            print("==================")
            pass
        return web_page_content

    # From that web page, I get the part of the html with the quote in it.
    def extract_quote_from_html(self,html_page,url):
        try:
            # Create the scraper element
            mushroomsoup = BeautifulSoup(html_page)
            for every_content in mushroomsoup.find('a',{'href':url}):
                every_content =  unicode(every_content).replace('<span class="decoration">',"")
                every_content =  unicode(every_content).replace('</span>',"")
                every_content =  unicode(every_content).replace('<br/>',"")
                every_content =  unicode(every_content).replace('&lt;',"<")
                every_content =  unicode(every_content).replace('&gt;',">")

                if every_content == '' or every_content == " ":
                    pass
                else:
                    elements.append(every_content)

            return elements
        except:
            pass

    # Then, I mix up both of them in order.
    def main(self,url):
        try:
            return self.extract_quote_from_html(self.get_web_page_content(url),url)
        except:
            pass
