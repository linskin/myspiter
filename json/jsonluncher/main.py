import json
import os

# 指定输入文件夹路径
input_folder = '../input'

# 指定输出文件夹路径
output_folder = '../output'

# 遍历输入文件夹中的所有文件
for filename in os.listdir(input_folder):
    # 拼接输入文件的完整路径
    input_file_path = os.path.join(input_folder, filename)
    # 检查路径是否为文件
    if os.path.isfile(input_file_path):
        # 构造输出文件路径（保持文件名不变）
        output_file_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.txt')
        file_content = ""
        # 打开输入文件
        with open(input_file_path, 'r', encoding='utf-8') as input_file:
            # 读取输入文件内容
            data = json.load(input_file)
            for item in data:
                # 将文章标题、作者、摘要和PDF链接添加到file_content变量中
                file_content += f"Title: {item['title']}\n"
                file_content += f"Authors: {', '.join(item['authors'])}\n"
                # file_content += f"Summary: {item['summary']}\n"
                # file_content += f"PDF URL: {item['pdf_url']}\n\n"
                file_content += f"HTML URL: {item['html_url']}\n\n"

        # 打开输出文件，如果不存在，则会创建该文件
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            # 将file_content内容写入输出文件
            output_file.write(file_content)
        print(f"File '{filename}' copied to '{output_folder}'.")
