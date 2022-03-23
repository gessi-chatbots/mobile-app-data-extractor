import scrapy
from scrapy import Request


class AlternativeSpider(scrapy.Spider):
    name = 'alternative'
    start_urls = [
        "https://www.alternativeto.net/software/osmand/about/"
    ]
    handle_httpstatus_list= [403]

    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'sec-ch-ua-platform': 'Windows',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-Dest': 'document',
            'sec-fetch-mode': 'navigate'

        }
        cookies = {
            'a2': '71%7Cfalse',
            'ARRAffinity': '628356fae902f3f844f9e9113bb6432b5013900ff654c4981f9460b163e412d2',
            'ARRAffinitySameSite': '628356fae902f3f844f9e9113bb6432b5013900ff654c4981f9460b163e412d2'
        }
        for url in self.start_urls:
            yield Request(url, headers=headers, method='GET', cookies=cookies)

    def parse(self, response):
        with open("log.txt",'w') as f:
            print(response.request.headers, file=f)
            print(response.headers, file=f)
        for features in response.css('div.badges link-color'):
            yield {
                "text": features.xpath("li/a()").get()
            }

