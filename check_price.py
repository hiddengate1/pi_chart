from datetime import datetime
import pytz
import scrapy
from scrapy.crawler import CrawlerProcess
import re
import csv

class SanpinetworkSpider(scrapy.Spider):
    name = "sanpinetwork"
    start_urls = [
        'https://sanpinetwork.com/'
    ]

    def parse(self, response):
        data = []
        utc_datetime = datetime.utcnow()
        intTime = utc_datetime.timestamp()
        buyPrice = response.selector.xpath('//*[@id="container"]/section[1]/div[1]/ul/li[1]/strong/text()').get()
        sellPrice = response.selector.xpath('//*[@id="container"]/section[1]/div[1]/ul/li[2]/strong/text()').get()
        data.append(intTime)
        data.append(re.sub(r'[^0-9]', '', buyPrice))
        data.append(re.sub(r'[^0-9]', '', sellPrice))
        with open('price.csv', 'a', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow(data)

if __name__ == "__main__":
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })

    process.crawl(SanpinetworkSpider)
    process.start()
