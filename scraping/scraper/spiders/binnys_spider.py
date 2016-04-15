import scrapy
from walmart_test.items import WalmartItem
from scrapy.http import Request

class BinnysSpider(scrapy.Spider):
	name = "binnys"
	allowed_domains = ["binnys.com"]
	start_urls = [
		"http://www.binnys.com/all/beer/1//500"
	]
	def start_requests(self):
	    for url in self.start_urls:
			yield Request(url, cookies={'PHPSESSID':'0llb9d1bm1m85dpij0tqsiav81'}, callback=self.parse)

	def parse(self, response):
		for sel in response.xpath('//body/div/div/div/div/div/div[contains(@class, \'row result\')]'):
			beer = str(sel.xpath('div/h3/a/text()').extract())[3:-2]
			price  = str(sel.xpath('div/div/div/div/div[contains(@class, \'prodPrice\')]/text()').extract())[3:-2]
			amountInfo = str(sel.xpath('div/div/div/div/div/text()').extract()[1])
			if len(price) > 1 and "oz" in amountInfo:
				print beer, price, amountInfo
#			if len(beer) > 5:
#				beer = beer[3:-2].split(",")
#				price = price[3:-2].strip().split(",")
#				if len(price) == 1:
#					price = price[0][26:]
#				else: 
#					price = price[1][5:-1].strip()
#				beerName = beer[0]
#				beerAmt = beer[1].split()[0]
#				if len(beer) > 2:
#					beerNum = beer[2].split()[0]
#				else:
#					beerNum = 1
#				print beerName, beerAmt, beerNum, price

