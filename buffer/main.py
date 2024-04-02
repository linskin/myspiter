import requests
from bs4 import BeautifulSoup
import os

# 定义函数用于下载 PDF 文件
# def download_pdf(url, folder):
#     response = requests.get(url)
#     if response.status_code == 200:
#         # 从 URL 中获取文件名
#         filename = url.split('/')[-1]
#         # 拼接本地文件路径
#         filepath = os.path.join(folder, filename)
#         # 保存 PDF 文件
#         with open(filepath, 'wb') as f:
#             f.write(response.content)
#         print(f"Downloaded {filename} successfully.")
#     else:
#         print(f"Failed to download {url}.")

# 网页 URL
url = "https://www.jos.org.cn/jos/article/issue/2022_33_5"
# # 下载保存 PDF 文件的文件夹
# pdf_folder = 'pdf_files'

# # 创建文件夹
# if not os.path.exists(pdf_folder):
#     os.makedirs(pdf_folder)

# 获取网页内容
response = requests.get(url)
# 获取网页内容的编码格式
encoding = response.encoding

# print(response.text)
with open("1.txt", "w", encoding=encoding) as file:
    file.write(response.text)

if response.status_code == 200:
    contents = ""
    # 使用 BeautifulSoup 解析 HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    # 找到所有的li
    links = soup.find_all('li')
    with open("2.txt", "w", encoding=encoding) as file:
        file.write(str(links))
    # print(links[47])
    # print(len(links))
    for link in links:
        # with open("2.txt", "w", encoding="utf-8") as file:
        # file.write(link)
        # href = link.get('href')
        contents += link.text + "\n"
    #     print(link)
    with open("3.txt", "w", encoding=encoding) as file:
        file.write(contents)

    with open("4.txt", "w", encoding=encoding) as file:
        for i, link in enumerate(links, start=1):
            file.write(str(i) + ": "+"\n")
            # print(i)
            a = link.find_all('a')
            # href = a['href']
            p = link.find_all('p')
            if a:
                for tag in a:
                    href = tag.get('href')
                    file.write("a: " + tag.text)
                    # print("a: " + tag.text)
                    if href is not None:
                        # print(href)
                        file.write("\n" + "href: " + href)
            if p:
                for tag in p:
                    # print("p: " + tag.text)
                    file.write("p: " + tag.text)
                    href = tag.get('href')
                    if href is not None:
                        # print(href)
                        file.write("\n" + "href: " + href)
            # print('\n')
            file.write('\n')

        # if href.endswith('.pdf'):
#         #     # 如果链接指向 PDF 文件，则下载
#         #     download_pdf(href, pdf_folder)
#  else:
#     print(f"Failed to fetch {url}.")
