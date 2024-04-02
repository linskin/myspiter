import json
import os

# from myproject.starter import run_pdf_spider
import myproject
from myproject.starter import run_pdf_spider

# 指定输入文件夹路径
input_folder = '../input'

# 指定输出文件夹路径
output_folder = '../output'

pdf_urls = []
# 遍历输入文件夹中的所有文件
for filename in os.listdir(input_folder):
    # 拼接输入文件的完整路径
    input_file_path = os.path.join(input_folder, filename)
    # 检查路径是否为文件
    if os.path.isfile(input_file_path):
        # 构造输出文件路径（保持文件名不变）
        output_file_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.txt')

        # 打开输入文件
        with open(input_file_path, 'r', encoding='utf-8') as input_file:
            # 读取输入文件内容
            data = json.load(input_file)
            for item in data:
                # 读取所有html网址
                pdf_url = "https://jos.org.cn/" + item['pdf_url']
                pdf_urls.append(pdf_url)
                # pdf_urls += f"PDF URL: {item['pdf_url']}\n\n"

        # 遍历网址列表，下载对应pdf
print(pdf_urls)

run_pdf_spider(pdf_urls)
# # 打开输出文件，如果不存在，则会创建该文件
# with open(output_file_path, 'w', encoding='utf-8') as output_file:
#     # 将file_content内容写入输出文件
#     output_file.write(pdf_urls)
# print(f"File '{filename}' copied to '{output_folder}'.")
