from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from myproject.spiders.html_spider import HtmlSpider
from myproject.spiders.json_spider import JsonSpider
# from myproject.spiders.pdf_spider import PdfSpider


def run_json_spider(urls):
    process = CrawlerProcess(get_project_settings())
    process.crawl(JsonSpider, urls=urls)
    process.start()


# def run_pdf_spider(urls):
#     process = CrawlerProcess()
#     process.crawl(PdfSpider, urls=urls)
#     process.start()


def run_html_spider(urls):
    process = CrawlerProcess(get_project_settings())
    process.crawl(HtmlSpider, urls=urls)
    process.start()


if __name__ == "__main__":
    # urls = [
    #     'https://www.jos.org.cn//jos/article/pdf/6908?st=article_issue',
    #     'https://www.jos.org.cn//jos/article/pdf/6935?st=article_issue',
    #     'https://www.jos.org.cn//jos/article/pdf/6810?st=article_issue',
    #     'https://www.jos.org.cn//jos/article/pdf/6835?st=article_issue',
    #     'https://www.jos.org.cn//jos/article/pdf/6902?st=article_issue'
    # ]
    # urls_str = ','.join(urls)
    # run_pdf_spider(urls_str)

    # start_urls = [
    #     'https://www.jos.org.cn/jos/article/issue/2024_35_9',
    #     'https://www.jos.org.cn/jos/article/issue/2024_35_8',
    #     'https://www.jos.org.cn/jos/article/issue/2024_35_7',
    #     'https://www.jos.org.cn/jos/article/issue/2024_35_6',
    #     'https://www.jos.org.cn/jos/article/issue/2024_35_5',
    #     'https://www.jos.org.cn/jos/article/issue/2024_35_4',
    #     'https://www.jos.org.cn/jos/article/issue/2024_35_3',
    #     'https://www.jos.org.cn/jos/article/issue/2024_35_2',
    #     'https://www.jos.org.cn/jos/article/issue/2024_35_1',
    # ]
    start_urls = ['https://jos.org.cn/html/2024/1/6908.htm',
                  'https://www.jos.org.cn/html/2024/2/6983.htm']
    # start_urls_str = ','.join()
    # run_json_spider(start_urls)
    run_html_spider(start_urls)

    # start_urls = [
    #     'https://www.jos.org.cn/jos/article/issue/2024_35_9',
    #     'https://www.jos.org.cn/jos/article/issue/2024_35_8',
    #     'https://www.jos.org.cn/jos/article/issue/2024_35_7',
    #     'https://www.jos.org.cn/jos/article/issue/2024_35_6',
    #     'https://www.jos.org.cn/jos/article/issue/2024_35_5',
    #     'https://www.jos.org.cn/jos/article/issue/2024_35_4',
    #     'https://www.jos.org.cn/jos/article/issue/2024_35_3',
    #     'https://www.jos.org.cn/jos/article/issue/2024_35_2',
    #     'https://www.jos.org.cn/jos/article/issue/2024_35_1',
    # ]
    # run_json_spider(start_urls)