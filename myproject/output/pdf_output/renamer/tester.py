import pdfplumber


# 目前只试过软件学报的文献
def extract_article_title_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = pdf.pages[0].extract_text()
        tmp_title = text.split('\n')[4]
        if tmp_title == '∗' or "*":
            tmp_title = text.split('\n')[3]
        end_title = ""
        for character in tmp_title:
            if character in '\\/:*?"<>|':
                continue
            else:
                end_title += character

    return end_title


if __name__ == "__main__":
    pdf_path = '.pdf'
    with pdfplumber.open(pdf_path) as pdf:
        text = pdf.pages[0].extract_text()
    title = text.split('\n')[4]
    print(title)
    title2 = extract_article_title_from_pdf(pdf_path)
    print(title2)
