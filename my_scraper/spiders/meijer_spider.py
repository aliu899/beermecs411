import scrapy
import sys
sys.path.append('/app')
from models import add_beer

class MeijerSpider(scrapy.Spider):
	name = "meijer"
	allowed_domains = ["meijer.com"]
	start_urls = [
		"https://www.meijer.com/catalog/search_command.cmd?page=13&keyword=beer&sort=1&rows=10000",
	]

	def parse(self, response):
		for sel in response.xpath('//body/div/div/div/div/div/div/div/div/ul/li'):
			beer = str(sel.xpath('div/div/div/div[contains(@class, \'prod-title\')]/a/text()').extract())
			price = str(sel.xpath('div/div/div/div[contains(@class, \'prod-price-sale\')]/div/text()[1]').extract())
			photo = str(sel.xpath('div/div/div/a/img/@src').extract())
			
			if len(beer) > 5:
				beer = beer[3:-2].split(",")
				photo = "http://" + photo[5:-2]
				
				price = price[3:-2].strip().split(",")
				if len(price) == 1:
					price = price[0][27:]
				else: 
					price = price[1][5:-1].strip()[1:]

				beerName = beer[0]
				beerAmt = beer[1].split()[0]
				if len(beer) > 2:
					beerNum = beer[2].split()[0]
				else:
					beerNum = 1

				if beerName.endswith("Root Beer"):
					beerName = beerName[:-9] + "Root beer"
				if beerName.endswith(" Single"):
					beerName = beerName[:-7]
				if beerName.endswith(" Beer"):
					beerName = beerName[:-5]
				beerName = beerName.replace("'", "")

				add_beer(beerName, photo, beerAmt, beerNum, price, "Meijer")
