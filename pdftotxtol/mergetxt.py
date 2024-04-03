import os
from datetime import datetime


def get_current_time():
    # 获取当前时间
    current_time = datetime.now()
    # 格式化输出当前时间
    formatted_time = current_time.strftime("%Y%m%d%H%M%S")
    return formatted_time


def mergetxt(input_folder, output_folder):
    # 构造输出文件路径（保持文件名不变）
    output_file_path = os.path.join(output_folder, get_current_time() + ".txt")
    # 遍历输入文件夹中的所有文件
    for filename in os.listdir(input_folder):
        # 拼接输入文件的完整路径
        input_file_path = os.path.join(input_folder, filename)
        # 检查路径是否为文件
        if os.path.isfile(input_file_path):
            # 打开输入文件
            with open(input_file_path, 'r', encoding='utf-8') as input_file:
                # 读取输入文件内容
                file_content = input_file.read()
            # 打开输出文件，如果不存在，则会创建该文件
            with open(output_file_path, 'a', encoding='utf-8') as output_file:
                # 将输入文件内容写入输出文件
                output_file.write('\n')
                output_file.write(file_content)


if __name__ == '__main__':
    # 指定输入文件夹路径
    input_folder = 'input'
    # 指定输出文件夹路径
    output_folder = 'output'
    mergetxt(input_folder, output_folder)
