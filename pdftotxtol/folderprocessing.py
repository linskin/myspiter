import os


def get_files_in_folder(folder_path):
    # 列出文件夹中的所有文件和子文件夹
    files = os.listdir(folder_path)
    file_paths = []
    for file in files:
        # 获取文件或子文件夹的完整路径
        file_path = os.path.join(folder_path, file)
        # 如果是文件，则将文件路径添加到列表中
        if os.path.isfile(file_path) and file_path.endswith('.pdf'):
            file_paths.append(file_path)
        # 如果是文件夹，则递归调用函数获取子文件夹中的文件路径
        elif os.path.isdir(file_path):
            file_paths.extend(get_files_in_folder(file_path))
    return file_paths


def get_twenty_files_every_times(file_paths):
    twenty_files = ""
    length = len(file_paths)
    if length >= 20:
        for i in range(20):
            twenty_files += (file_paths[0] + "\n" if i < 19 else file_paths[0])
            file_paths.pop(0)
    elif length < 20:
        for i in range(len(file_paths)):
            twenty_files += (file_paths[0] + "\n" if i < len(file_paths) - 1 else file_paths[0])
            file_paths.pop(0)
    return twenty_files
