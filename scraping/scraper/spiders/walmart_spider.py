import scrapy
from walmart_test.items import WalmartItem

class WalmartSpider(scrapy.Spider):
	name = "walmart"
	allowed_domains = ["walmart.com"]
	start_urls = [
		"http://www.walmart.com/"
	]

	def parse(self, response):
		for sel in response.xpath('title'):
			print(sel)	
