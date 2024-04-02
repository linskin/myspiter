from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from myproject.spiders.pdf_spider import PdfSpider
from myproject.spiders.html_spider import HtmlSpider
from myproject.spiders.json_spider import JsonSpider
import json
import os


def run_json_spider(urls):
    process = CrawlerProcess(get_project_settings())
    process.crawl(JsonSpider, urls=urls)
    process.start()


def run_pdf_spider(urls):
    process = CrawlerProcess()
    process.crawl(PdfSpider, urls=urls)
    process.start()


def run_html_spider(urls):
    process = CrawlerProcess(get_project_settings())
    process.crawl(HtmlSpider, urls=urls)
    process.start()


def run_pdf_spider_for_files(input_folder):
    # 遍历输入文件夹中的所有文件
    pdf_urls = []
    for filename in os.listdir(input_folder):
        # 拼接输入文件的完整路径
        input_file_path = os.path.join(input_folder, filename)
        # 检查路径是否为文件
        if os.path.isfile(input_file_path):
            # 打开输入文件
            with open(input_file_path, 'r', encoding='utf-8') as input_file:
                # 读取输入文件内容
                data = json.load(input_file)
                for item in data:
                    # 读取所有pdf网址
                    pdf_url = "https://jos.org.cn/" + item['pdf_url']
                    pdf_urls.append(pdf_url)
    # 遍历网址列表，下载对应pdf
    # print(pdf_urls)
    run_pdf_spider(pdf_urls)


if __name__ == "__main__":
    # 指定输入文件夹路径
    input_folder = 'output/json_output'
    run_pdf_spider_for_files(input_folder)
