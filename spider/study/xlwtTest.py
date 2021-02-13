# Coding : utf-8
# Author : chyh
# Date   : 2021/2/13 23:36

import xlwt


def writeToExcel():
    workBook = xlwt.Workbook(encoding="utf-8")

    workSheet1 = workBook.add_sheet("sheet1")
    workSheet1.write(0, 0, "hello")
    workBook.save("test.xls")


if __name__ == '__main__':
    writeToExcel()
