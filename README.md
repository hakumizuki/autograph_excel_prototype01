# 必要環境
- windows OS
- いい感じのエディタ(VSCode推奨)
- Python3.X

# 使い方
0. -準備-
コマンドプロンプトを起動したら、'autograph_excel_prototype01'フォルダにいることを確認してください(pdwコマンドを実行して....../....../autograph_excel_prototype01になっていればOK)

1. -確認-
'converted_csv_files'フォルダ、'excel_graphs/converted_csv_files'フォルダが存在することを確認

2. -.csvに変換-
'experiment_data'フォルダにcsvに変換したいGRPファイルを全て入れ、'grpconverter.py'の「設定」の値を変更したら、コマンドプロンプトで'python3 grpconverter.py'を実行

3. -グラフ化して、.xlsxに変換-
'autograph.py'の諸々の「設定」をしたら、コマンドプロンプトで'python_exe.bat'を実行