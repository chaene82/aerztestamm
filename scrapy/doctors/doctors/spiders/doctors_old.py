import scrapy

class DoctorsSpider(scrapy.Spider):
    name = "doctors"
    allowed_domains = ["doktor.ch"]
    start_urls = [
        "http://www.doctor.ch/doctors/doctors_k_zh",
    ]

    def parse(self, response):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_dir_contents)
            print "Doktor gefunden"

    def parse(self, response):
        filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
