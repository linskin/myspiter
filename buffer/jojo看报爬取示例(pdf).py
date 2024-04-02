import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

from bs4 import BeautifulSoup

url = 'https://reader.jojokanbao.cn/rmrb'
down_load_dir = os.path.abspath(".")  # 下载目录设为当前目录

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

browser.get(url)

# 输入日期并回车
# date_input = browser.find_element_by_class_name('el-input__inner')
date_input = browser.find_element(By.CLASS_NAME, 'el-input__inner')
date_input.clear()
date_input.send_keys('1976-10-09')
date_input.send_keys(Keys.ENTER)

# 使用显式等待等待链接出现
try:
    link_element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div.el-col.el-col-24.el-col-xs-24.el-col-sm-12.el-col-md-12'
                                                         '.el-col-lg-12.el-col-xl-12 a'))
    )
    link = link_element.get_attribute('href')
    # link = 'https://www.jos.org.cn/jos/article/pdf/6908'
    print("PDF链接：", link)
    # link = 'https://www.jos.org.cn/jos/article/pdf/6908'
    # 使用Selenium的requests模块下载PDF文件
    response = requests.get(link)
    filename = os.path.join(down_load_dir, 'downloaded_file.pdf')
    with open(filename, 'wb') as f:
        f.write(response.content)
    print("PDF 下载完成:", filename)
    # # 下载PDF文件
    # browser.get(link)
    # print("PDF 下载完成")
except Exception as e:
    print("发生异常:", e)

# 关闭浏览器
browser.quit()
