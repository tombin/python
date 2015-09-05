from lxml import html
import requests
import urlparse
import sys

class Scrape:
    def __init__(self):
        self.currentUrlData = 0

    def parseUrl(self, url): 
        urldata = urlparse.urlparse(url)
        if (not urldata.scheme and not urldata.netloc and  
           not self.currentUrlData.scheme and not self.currentUrlData.netloc):
            print "bad url passed into parseUrl()"
            sys.exit()
        if not urldata.scheme:
           urldata = urldata._replace(scheme = self.currentUrlData.scheme)
        if not urldata.netloc:
           urldata = urldata._replace(netloc = self.currentUrlData.netloc)
        return urldata
            
    def getPage(self, url):
        self.currentUrlData = self.parseUrl(url)
        resp = requests.get(url)
        return resp.text

    def urlScrape(self, content):
        # get all the urls in a page
        scrapedUrls = []
        page = html.fromstring(content)
        print page
        for item in page.xpath('//a/@href'):
            url = self.parseUrl(item)
            scrapedUrls.append(url.geturl())
	return scrapedUrls

    def tableScrape():
        # scrape all the tables from a page and serialize to disk
        pass

    def imageScrape(self):
        # download and store all images from a page
        pass


