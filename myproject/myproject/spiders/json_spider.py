import json
import scrapy
import os



class JsonSpider(scrapy.Spider):
    name = 'json_spider'

    def __init__(self, urls=None, *args, **kwargs):
        super(JsonSpider, self).__init__(*args, **kwargs)
        self.start_urls = urls if urls else []

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        url_parts = response.url.split('/')
        # 获取项目根目录路径
        project_dir = os.path.abspath(os.path.dirname(__file__))
        filename = f"{project_dir}/../../output/json_output/{url_parts[-3]}_{url_parts[-2]}_{url_parts[-1]}.json"
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        articles_data = []
        for article in response.xpath("//li[@class='article_line']"):
            article_data = {
                'title': article.xpath(".//div[@class='article_title']/a/text()").get(),
                'authors': article.xpath(".//p[@class='article_author']/span/a/text()").getall(),
                'summary': article.xpath(".//div[@class='abstract_body']/p/text()").get(),
                'pdf_url': article.xpath(".//a[@class='btn_pdf']/@href").get(),
                'html_url': article.xpath(".//a[@class='btn_html']/@href").get(),
            }
            articles_data.append(article_data)

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(json.dumps(articles_data, ensure_ascii=False, indent=4))
