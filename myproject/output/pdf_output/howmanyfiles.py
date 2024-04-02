import os


def count_files_in_folder(folder_path):
    # 获取文件夹中的文件列表
    file_list = os.listdir(folder_path)
    # 计算文件列表的长度
    file_count = len(file_list)
    return file_count


if __name__ == "__main__":
    # 指定文件夹路径
    folder_path = '.'
    # 获取文件夹中文件的数量
    num_files = count_files_in_folder(folder_path)
    print(f"There are {num_files} files in the folder.")
