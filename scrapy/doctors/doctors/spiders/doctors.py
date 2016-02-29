import scrapy
from bs4 import BeautifulSoup


class DoctorsSpider(scrapy.Spider):
    name = "doctors"
    allowed_domains = ["doktor.ch"]
    start_urls = [
        "http://www.doktor.ch/roentgenaerzte/roentgenaerzte_k_zh.html"
    ]

    def parse(self, response):
        hxs = scrapy.Selector(response)
        # extract all links from page
        all_links = hxs.xpath('*//a[@class="novip-firmen-name"]/@href').extract()
        # iterate over links
        for link in all_links:
            url_arzt = response.urljoin(link)
            yield scrapy.http.Request(url_arzt, callback=self.parse_dir_contents)
#            print url_arzt
        pass
 
    def print_this_link(self, link):
        print "Link --> {this_link}".format(this_link=link)

    def parse_dir_contents(self, response):
        yield {
            'firmaname' : ''.join(response.xpath('//head/title/text()').extract()).strip(),
            'facharzttitle' : ''.join(response.xpath("//td[contains(text(),'Facharzt')]/following-sibling::td[1]/text()").extract()).strip(),
            'diplom' : ''.join(response.xpath("//td[contains(text(),'Diplom')]/following-sibling::td[1]/text()").extract()).strip(),
            'gln-nummer' :  ''.join(response.xpath("//td[contains(text(),'GLN-Nummer')]/following-sibling::td[1]/text()").extract()).strip(),
            'tel' :       response.xpath("//td[contains(text(),'Tel')]/text()").extract(),
            'email' :     response.xpath("//td[contains(text(),'E-Mail')]/text()").extract(),
            'homepage' :  response.xpath("//td[contains(text(),'Homepage')]/text()").extract(),
#            'table' :     response.xpath("//*[@id='main-single']/table").extract(),
        }
