import pdfplumber
import os

# 提取pdf表格整理成html表格
def extract_table():
    latest_pdf = get_latest_pdf()
    if not latest_pdf:
        return
    pdf = pdfplumber.open(latest_pdf)
    table_html = "<table border=1>"
    for page in pdf.pages:
        for table in page.extract_tables():
            for i, item in enumerate(table):
                table_html += "<tr>"
                if i == 0 and table_html.find("<th>") == -1:
                    for value in item:
                        table_html += "<th>" + value + "</th>"
                else :
                    for value in item:
                        table_html += "<td>" + value + "</td>"
                table_html += "</tr>"
    table_html += "</table>"
    return table_html

# 获取最新的pdf文件
def get_latest_pdf():
    pdf_dir = "C:/pdf"
    dir_list = os.listdir(pdf_dir)
    if dir_list:
        dir_list.sort(key = lambda fn : os.path.getmtime(pdf_dir + '/'+ fn), reverse = True)
        return pdf_dir + "/" + dir_list[0]


if __name__ == "__main__":
    print(extract_table())