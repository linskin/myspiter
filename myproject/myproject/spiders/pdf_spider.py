# import scrapy
#
#
# class PdfSpider(scrapy.Spider):
#     name = 'pdf_spider'
#
#     def __init__(self, urls=None, *args, **kwargs):
#         super(PdfSpider, self).__init__(*args, **kwargs)
#         self.start_urls = urls.split(',') if urls else []
#
#     def start_requests(self):
#         for url in self.start_urls:
#             yield scrapy.Request(url, callback=self.parse)
#
#     def parse(self, response):
#         # 获取PDF文件的URL
#         pdf_url = response.url
#
#         # 提取PDF文件名
#         pdf_name = pdf_url.split('/')[-1]
#
#         # 下载PDF文件
#         yield {
#             'file_urls': [pdf_url],
#             'file_name': pdf_name
#         }


# import scrapy
# from scrapy.crawler import CrawlerProcess
# from scrapy.pipelines.files import FilesPipeline
# from scrapy.utils.project import get_project_settings
#
#
# class PdfSpider(scrapy.Spider):
#     name = 'pdf_spider'
#     start_urls = [
#             'https://www.jos.org.cn//jos/article/pdf/6908?st=article_issue',
#             'https://www.jos.org.cn//jos/article/pdf/6935?st=article_issue',
#             'https://www.jos.org.cn//jos/article/pdf/6810?st=article_issue',
#             'https://www.jos.org.cn//jos/article/pdf/6835?st=article_issue',
#             'https://www.jos.org.cn//jos/article/pdf/6902?st=article_issue'
#         ]
#     # def __init__(self, urls=None, *args, **kwargs):
#     #     super(PdfSpider, self).__init__(*args, **kwargs)
#     #     self.start_urls = urls if urls else []
#     #
#     # def start_requests(self):
#     #     for url in self.start_urls:
#     #         yield scrapy.Request(url, callback=self.parse)
#
#     def parse(self, response):
#         # 提取PDF文件的URL
#         pdf_url = response.url
#
#         # 提取PDF文件名
#         pdf_name = pdf_url.split('/')[-1]
#
#         # 返回包含文件URL和文件名的字典
#         yield {
#             'file_urls': [pdf_url],
#             'pdf_name': pdf_name
#         }


# class CustomFilesPipeline(FilesPipeline):
#     def file_path(self, request, response=None, info=None, *, item=None):
#         return item['pdf_name']
#
# import scrapy
#
# class PdfSpider(scrapy.Spider):
#     name = 'pdf_spider'
#     start_urls = ['https://jos.org.cn/jos/home?id=20210909102755001&name=%E4%B8%BB%E9%A1%B5']  # 替换为你要爬取的网页
#
#     def parse(self, response):
#         # 提取所有的<a>标签
#         for link in response.css('a'):
#             # 获取链接的href属性
#             href = link.attrib['href']
#             # 检查链接是否以'.pdf'结尾
#             if href.endswith('.pdf'):
#                 # 构造PDF文件的绝对链接
#                 pdf_url = response.urljoin(href)
#                 # 下载PDF文件
#                 yield scrapy.Request(pdf_url, callback=self.save_pdf)
#
#     def save_pdf(self, response):
#         # 获取PDF文件名
#         filename = response.url.split('/')[-1]
#         # 保存PDF文件
#         with open(filename, 'wb') as f:
#             print("save to %s" % filename)
#             f.write(response.body)
#         self.log('Saved file %s' % filename)
#

# def run_spider(urls):
#     process = CrawlerProcess(get_project_settings())
#     process.crawl(PdfSpider, urls=urls)
#     process.start()
#
#
# if __name__ == "__main__":
#     urls = [
#         'https://www.jos.org.cn//jos/article/pdf/6908?st=article_issue',
#         'https://www.jos.org.cn//jos/article/pdf/6935?st=article_issue',
#         'https://www.jos.org.cn//jos/article/pdf/6810?st=article_issue',
#         'https://www.jos.org.cn//jos/article/pdf/6835?st=article_issue',
#         'https://www.jos.org.cn//jos/article/pdf/6902?st=article_issue'
#     ]
#     run_spider(urls)
import scrapy
from scrapy.http import Request


# def save_pdf(response):
#     # 提取PDF文件名
#     file_name = response.url.split('/')[-1]
#     # 保存PDF文件到本地
#     with open(file_name, 'wb') as f:
#         f.write(response.body)
#
#
# class PDFSpider(scrapy.Spider):
#     name = 'pdf_spider'
#     start_urls = ['https://www.jos.org.cn//jos/article/pdf/6908?st=article_issue']  # 替换为你要爬取的网页URL
#     custom_settings = {
#         'ROBOTSTXT_OBEY': False
#     }
#     def parse(self, response):
#         # 在这里编写代码来提取PDF链接
#         pdf_links = response.css('a[href$=".pdf"]::attr(href)').extract()
#
#         for pdf_link in pdf_links:
#             # 构造一个Request对象，指定下载PDF文件的回调函数
#             yield Request(pdf_link, callback=save_pdf)

import scrapy

class PdfSpider(scrapy.Spider):
    name = 'pdf_spider'
    start_urls = ['https://www.jos.org.cn//jos/article/pdf/6908?st=article_issue']  # 替换为你的目标PDF预览页的网址

    def parse(self, response):
        # 提取PDF文件的直接下载链接
        pdf_url = response.css('a[href$=".pdf"]::attr(href)').get()
        if pdf_url:
            # 下载PDF文件
            yield scrapy.Request(response.urljoin(pdf_url), callback=self.save_pdf)

    def save_pdf(self, response):
        # 获取PDF文件名
        filename = response.url.split('/')[-1]
        # 保存PDF文件
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
