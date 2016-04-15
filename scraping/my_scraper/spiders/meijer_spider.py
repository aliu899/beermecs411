import scrapy

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
			if len(beer) > 5:
				beer = beer[3:-2].split(",")
				price = price[3:-2].strip().split(",")
				if len(price) == 1:
					price = price[0][26:]
				else: 
					price = price[1][5:-1].strip()
				beerName = beer[0]
				beerAmt = beer[1].split()[0]
				if len(beer) > 2:
					beerNum = beer[2].split()[0]
				else:
					beerNum = 1
				print beerName, beerAmt, beerNum, price


