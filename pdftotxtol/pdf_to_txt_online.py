import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def pdf_to_txt_online(pdf_file_path, driver):
    # 显式等待页面加载完成
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "fileSelector"))
    )

    # 找到上传文件的 input 元素，并上传 PDF 文件
    upload_input = driver.find_element(By.XPATH, "//input[@type='file']")
    upload_input.send_keys(pdf_file_path)

    # 显式等待文件上传完成
    download_button = WebDriverWait(driver, 150).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='下载所有']"))
    )
    download_button.click()

    # 等待下载完成
    time.sleep(30)

    clear_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='清除列队']"))
    )

    clear_button.click()
