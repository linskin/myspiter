import os
import scrapy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))  # 获取上上级目录
down_load_dir = os.path.join(project_dir, 'output', 'pdf_output')  # 下载目录设为目标目录

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ['enable-automation'])
prefs = {
    "download.default_directory": down_load_dir,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True
}
options.add_experimental_option('prefs', prefs)
options.add_argument("--disable-blink-features=AutomationControlled")
browser = webdriver.Chrome(options=options)

# 在打开网页前，设置无头模式，以避免页面跳转检测
browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})


class PdfSpider(scrapy.Spider):
    name = 'pdf_spider'

    def __init__(self, urls=None, *args, **kwargs):
        super(PdfSpider, self).__init__(*args, **kwargs)
        self.start_urls = urls if urls else []

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        # 使用浏览器打开网页
        browser.get(response.url)

        # 使用显式等待等待链接出现
        link_element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                                            'div.el-col.el-col-24.el-col-xs-24.el-col-sm-12.el-col-md-12.el-col-lg-12'
                                            '.el-col-xl-12 a'))
        )
        link = link_element.get_attribute('href')

        # 下载PDF文件
        browser.get(link)

        # 关闭浏览器
        browser.quit()
