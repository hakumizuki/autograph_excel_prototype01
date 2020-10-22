# -*- coding: utf-8 -*-

import pathlib

# 「設定」
LINES_TO_POP = 10 # 何行目までを削除するかこの数値を変更して決めてください

# csv拡張子に変換と掃除
num = 0
for path in pathlib.Path("experiment_data").iterdir():
    if path.is_file():
        num += 1
        ff = open("converted_csv_files/converted{}.csv".format(num),'w')
        with open(path, "r") as current_file:
            lines = current_file.readlines()
            for i in range(LINES_TO_POP):
                lines.pop(0)
            ff.writelines(lines)
            print(current_file.read())
            current_file.close()


# with open("experiment_data/FILE001.GRP", "r") as answer:
#     print(answer.read())
#     answer.close()