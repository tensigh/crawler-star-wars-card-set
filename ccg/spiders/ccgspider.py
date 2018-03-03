# Original code from: https://blogs.sequoiainc.com/python-web-crawling-with-scrapy/
# His code didn't work on my system so I modified it to work for me.

import scrapy
from urllib import parse as urlparse
from ccg.items import CardImage

class CcgSpider(scrapy.Spider):  
  name = "ccg"
#  allowed_domains = "starwarsccg.org"
  start_urls = [
    "http://www.starwarsccg.org/cardlists/PremiereType.html"
  ]

  seen_urls = []

  def parse(self, response):
    title = response.xpath('//head/title/text()').extract()[0]
    for sel in response.xpath('//a'):
      link = str(sel.xpath('@href').extract()[0])
      if (link.endswith('.gif')):
        cardImage = CardImage()
        cardImage['page_title'] = title
        cardImage['image_urls'] = ['http://www.starwarsccg.org/cardlists/' + link]
        yield cardImage
      if (not link.startswith('V') and link.endswith('Type.html')):
        if (not link in self.seen_urls):
          self.seen_urls.append(link) 
          yield scrapy.Request(urlparse.urljoin('http://www.starwarsccg.org/cardlists/', link), callback=self.parse)