from selenium import webdriver

from pdf_to_txt_online import pdf_to_txt_online
from folderprocessing import get_files_in_folder
from folderprocessing import get_twenty_files_every_times


def main_start(folder_path):
    file_paths = get_files_in_folder(folder_path)

    # 启动浏览器
    driver = webdriver.Chrome()  # 或者使用其他浏览器，需要相应的驱动程序
    # 打开网站
    driver.get("https://pdftotext.com/zh/")

    while len(file_paths):
        twenty_file_paths = get_twenty_files_every_times(file_paths)
        pdf_to_txt_online(twenty_file_paths, driver)

    # 关闭浏览器
    driver.quit()


if __name__ == "__main__":
    folder_path = "G:\JetBrains\jetBrain_WorkSpeace\PychamProjects\myspiter\myproject\output\pdf_output\软件学报2024"  # 替换为实际的文件夹路径
    main_start(folder_path)
