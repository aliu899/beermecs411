import scrapy
import sys
sys.path.append('/app')
from models import add_beer
from scrapy.http import Request

class BinnysSpider(scrapy.Spider):
	name = "binnys"
	allowed_domains = ["binnys.com"]
	start_urls = [
		"http://www.binnys.com/all/beer/1//1000"
	]
	def start_requests(self):
	    for url in self.start_urls:
			yield Request(url, cookies={'PHPSESSID':'0llb9d1bm1m85dpij0tqsiav81'}, callback=self.parse)

	def parse(self, response):
		for sel in response.xpath('//body/div/div/div/div/div/div[contains(@class, \'row result\')]'):
			beer = str(sel.xpath('div/h3/a/text()').extract())[3:-2]
			beer = beer.replace("'", "")
			beer = beer.replace("%", "%%")
			price  = str(sel.xpath('div/div/div/div/div[contains(@class, \'prodPrice\')]/text()').extract())[4:-2]
			photo = str(sel.xpath('div/div[contains(@class, \'image\')]/a/div/div/img/@src').extract())[3:-2]
			amountInfo = str(sel.xpath('div/div/div/div/div/text()').extract()[1])
			if len(price) > 1 and "oz" in amountInfo:
				packIndex = amountInfo.find(" Pack")
				if packIndex > 0:
					num = amountInfo[:packIndex].strip()
					amountInfo = amountInfo[packIndex + 9:]
					ozIndex = amountInfo.find("oz")
					amt = amountInfo[:ozIndex].strip()
				else:
					num = 1
					ozIndex = amountInfo.find("oz")
					amt = amountInfo[:ozIndex]
				add_beer(beer, photo, amt, num, price, "Binnys")

