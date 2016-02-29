# -*- coding: utf-8 -*-
import scrapy


class DoctorslistSpider(scrapy.Spider):
    name = "doctorslist"
    allowed_domains = ["doktor.ch"]
    start_urls = (
        'http://www.doktor.ch/allgemeinaerzte/allgemeinaerzte_k_ag.html',
        'http://www.doktor.ch/allgemeinaerzte/allgemeinaerzte_k_zh.html',
        'http://www.doktor.ch/allgemeinaerzte/allgemeinaerzte_k_tg.html',
        'http://www.doktor.ch/allgemeinaerzte/allgemeinaerzte_k_sg.html',
        'http://www.doktor.ch/allgemeinaerzte/allgemeinaerzte_k_gl.html',
        'http://www.doktor.ch/allgemeinaerzte/allgemeinaerzte_k_gr.html',
        'http://www.doktor.ch/allgemeinaerzte/allgemeinaerzte_k_zg.html',
    )


    def parse(self, response):
        hxs = scrapy.Selector(response)
        # extract all links from page
        doctors = hxs.xpath('*//table[@class="novip"]')
        # iterate over links
        for doctor in doctors:
           yield {
               'link' : doctor.xpath('*//a[@class="novip-firmen-name"]/@href').extract(),
               'name' : ''.join(doctor.xpath('*//a[@class="novip-firmen-name"]/text()').extract()).strip(),
               'title' : ''.join(doctor.xpath('./tr[2]/td/text()').extract()).strip(),
               'address' : ''.join(doctor.xpath('./tr[3]/td[1]/text()').extract()).strip(),
               'tel'  : ''.join(doctor.xpath('*//td[@class="novip-right-telefon"]/text()').extract()).strip(),
               'fax'  : ''.join(doctor.xpath('*//td[@class="novip-right-fax"]/text()').extract()).strip(),
           }
        print doctor.xpath('./tr[2]/td/text()').extract(),
        pass


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

