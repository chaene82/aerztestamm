import scrapy
from bs4 import BeautifulSoup


class DoctorsSpider(scrapy.Spider):
    name = "doctors"
    allowed_domains = ["doktor.ch"]
    start_urls = [
        'http://www.doktor.ch/allgemeinaerzte/allgemeinaerzte_k_ag.html',
        'http://www.doktor.ch/allgemeinaerzte/allgemeinaerzte_k_zh.html',
        'http://www.doktor.ch/allgemeinaerzte/allgemeinaerzte_k_tg.html',
        'http://www.doktor.ch/allgemeinaerzte/allgemeinaerzte_k_sg.html',
        'http://www.doktor.ch/allgemeinaerzte/allgemeinaerzte_k_gl.html',
        'http://www.doktor.ch/allgemeinaerzte/allgemeinaerzte_k_gr.html',
        'http://www.doktor.ch/allgemeinaerzte/allgemeinaerzte_k_zg.html',

#        'http://www.doktor.ch/aerzte/aerzte_k_zh',
#        'http://www.doktor.ch/aerzte/aerzte_k_tg',
#        'http://www.doktor.ch/aerzte/aerzte_k_sg',
#        'http://www.doktor.ch/aerzte/aerzte_k_ag',
#        'http://www.doktor.ch/aerzte/aerzte_k_ai',
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
            'link' : response.url,
            'firmaname' : ''.join(response.xpath('//head/title/text()').extract()).strip(),
            'firmaname2': ''.join(response.xpath('//*[@id="main-single"]/table/tr[6]/td/text()').extract()).strip(),
            'facharzttitle' : ''.join(response.xpath("//td[contains(text(),'Facharzt')]/following-sibling::td[1]/text()").extract()).strip(),
            'diplom' : ''.join(response.xpath("//td[contains(text(),'Diplom')]/following-sibling::td[1]/text()").extract()).strip(),
            'gln-nummer' :  ''.join(response.xpath("//td[contains(text(),'GLN-Nummer')]/following-sibling::td[1]/text()").extract()).strip(),
            'tel' :       response.xpath("//td[contains(text(),'Tel')]/text()").extract(),
            'email' :     ''.join(response.xpath("//td[contains(text(),'E-Mail')]/a[contains(text(),'@')]/text()").extract()).strip(),
            'homepage' :  response.xpath("//td[contains(text(),'Homepage')]/text()").extract(),
#            'table' :     response.xpath("//*[@id='main-single']/table").extract(),
        }
