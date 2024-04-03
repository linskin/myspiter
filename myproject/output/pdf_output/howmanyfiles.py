import os


def count_file_types(folder_path, include_subfolders=True):
    file_types = {}
    # 遍历文件夹及其子文件夹中的所有文件
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            # 获取文件的扩展名
            _, ext = os.path.splitext(file_name)
            # 去除扩展名中的点号
            ext = ext[1:]
            # 统计文件类型及其数量
            if ext:
                file_types[ext] = file_types.get(ext, 0) + 1
        # 如果不包含子文件夹，则跳出循环，只统计当前文件夹中的文件类型
        if not include_subfolders:
            break

    return file_types


def main():
    # 获取当前文件夹路径
    current_folder = os.getcwd()
    # 提示用户选择是否包含子文件夹
    include_subfolders_input = input("是否包含子文件夹？(y/n): ").strip().lower()
    include_subfolders = include_subfolders_input == 'y'
    file_types = count_file_types(current_folder, include_subfolders)

    print("当前文件夹及其子文件夹中有以下类型的文件及其数量：")
    for file_type, count in file_types.items():
        print(f"{file_type}: {count} 个")


if __name__ == "__main__":
    main()
