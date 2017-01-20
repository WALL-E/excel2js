#!/usr/local/bin/python2.7
#-*- coding: utf8 -*-

import os
import sys
import json
import ast

import xlrd


def convert(excel, js):
    bk = xlrd.open_workbook(excel)
    # shxrange = range(bk.nsheets)
    try:
        sh = bk.sheet_by_name("Sheet1")
    except:
        print "no sheet in %s named Sheet1" % (excel)

#获取行数
    nrows = sh.nrows
#获取列数
    ncols = sh.ncols
#print "nrows %d, ncols %d" % (nrows,ncols)

    cases = []
#获取各行数据
    for i in range(1, nrows):
        case = {}
        for j in range(0, ncols):
            cell_key = sh.cell_value(0, j)
            if isinstance(cell_key, unicode):
                cell_key = cell_key.encode("utf-8")
            cell_val = sh.cell_value(i, j)
            if isinstance(cell_val, unicode):
                cell_val = sh.cell_value(i, j).encode("utf-8")
                cell_val = "".join(cell_val.split("\n"))
                try:
                    cell_val = ast.literal_eval(cell_val)
                except SyntaxError:
                    pass
                except ValueError:
                    pass
            case[cell_key] = cell_val
        cases.append(case)

    with open(js, "w") as f:
        f.write("\n")
        f.write("cases = ")
        dump = json.dumps(cases, indent=4, separators=(',', ': '), ensure_ascii=False, sort_keys=True)
        f.write(dump)
        f.write(";")
        f.write("\n\n")
        f.write("module.exports = cases;")


def main():
    if len(sys.argv) < 3:
        print "%s excel_file js_file" % (sys.argv[0])
        sys.exit(1)

    excel = sys.argv[1]
    js = sys.argv[2]

    if not os.path.exists(excel):
        print "%s is not exists" % (excel)
        sys.exit(2)

    convert(excel, js)


if __name__ == '__main__':
    main()
