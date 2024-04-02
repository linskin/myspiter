import os
import pdfplumber


# 目前只试过软件学报的文献
def extract_article_title_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = pdf.pages[0].extract_text()
        tmp_title = text.split('\n')[4]
        if tmp_title == '∗':
            tmp_title = text.split('\n')[3]
        end_title = ""
        for character in tmp_title:
            if character in '\\/:*?"<>|':
                continue
            else:
                end_title += character

    return end_title


if __name__ == "__main__":
    # 指定 PDF 文件夹路径
    pdf_folder = '../软件学报2024'
    # 遍历 PDF 文件夹中的所有文件
    for filename in os.listdir(pdf_folder):
        # 拼接 PDF 文件的完整路径
        pdf_path = os.path.join(pdf_folder, filename)
        # 检查路径是否为文件
        if os.path.isfile(pdf_path) and pdf_path.endswith('.pdf'):
            # 提取文章标题
            article_title = extract_article_title_from_pdf(pdf_path)
            print(article_title)
            # # 修改文件名为文章标题
            # new_filename = f"{article_title}.pdf"
            # # 重命名文件
            # os.rename(pdf_path, os.path.join(pdf_folder, new_filename))
            # print(f"Renamed {pdf_path} to {new_filename}")
