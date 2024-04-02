import json
import os
import scrapy


class HtmlSpider(scrapy.Spider):
    name = 'html_spider'

    def __init__(self, urls=None, *args, **kwargs):
        super(HtmlSpider, self).__init__(*args, **kwargs)
        self.start_urls = urls if urls else []

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        url_parts = response.url.split('/')
        # 获取项目根目录路径
        project_dir = os.path.abspath(os.path.dirname(__file__))
        filename = f"{project_dir}/../../output/html_output/{url_parts[-3]}_{url_parts[-2]}_{url_parts[-1]}.json"
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        articles_data = []
        for article in response.xpath("//div[@class='article']"):
            article_data = {
                'title': article.xpath(".//div[@class='article_title_cn']/text()").get(),
                'authors_cn': article.xpath(".//span[@class='author_CN']/text()").getall(),
                'authors_en': article.xpath(".//span[@class='author_EN']/text()").getall(),
                'summary': article.xpath(".//div[@class='abs']/text()").getall(),
                # 'summary_en': article.xpath(".//div[@class='abs']/text()").get(),
                'keywords': article.xpath(".//div[@class='key']/span[@class='keyword']/text()").getall(),
                'body': article.xpath(".//div[@class='article_body']/p/text()").getall(),
                # 'pdf_url': article.xpath(".//a[@class='btn_pdf']/@href").get(),
                # 'html_url': article.xpath(".//a[@class='btn_html']/@href").get(),
            }
            articles_data.append(article_data)

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(json.dumps(articles_data, ensure_ascii=False, indent=4))
