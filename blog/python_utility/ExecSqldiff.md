---
layout: adv_job_python
title: Python & SQLite3を活用してデータベース差分抽出をしよう
description: データベース、差分検出、SQLite3、Python、sqldiff
lang: ja_JP
---
## SQLite3について
こんにちは、netchiraです。

今回は、Pythonで利用可能なsqlite3についてお届けします。


### 前提条件
- Python 3.7 を使用
- 開発環境として Anaconda および Spyderを使用
- Windows 10 (64bit)

### データベース活用に手を出したい
最近、仕事をしていてExcelでデータ管理をするのがつらいなーと感じることがありまして
もうそろそろデータベースに手を出したいと思っていたのですが、何から手を付けていいか分からず躊躇していました。
が、私、一大決意しまして、土日を使ってトライしてみました。

といっても、Pythonのlite3を使ってExcelの特定の行をデータベースに登録する、みたいなことから着手している次第です。(現在進行形)
これに関しては、また別の記事で、記事にしたいと思っています。

しかし、結局、色んな情報を「データベース形式に変換」しても大して役に立たないことが分かったんですよね。
もしかしたらデータベースの有識者に言わせれば「色んな情報をデータベース形式でまとめられている」だけで意義があるのかもしれないのですが、
データベース初心者からすると、なにがどう役立つのかが分からず、ちょっと困惑していました。

そして、ある日、ふと思いついたことがありまして、データベースの差分比較ができると多少便利になるのかなと感じました。
(Excelの比較って、なにかと難しいじゃないですか。セルの単純比較したからと言って上手く差分が抽出できるとも限らないし。。。)

そこで少し調べてみますと、SQLiteのwebサイトに
- sqldiff.exe
- sqlite3_analyzer.exe
というものがあることを知りました！

これは私の探していたものでは！と期待を込めて早速いじってみました。

[SQLite sqldiff](https://www.sqlite.org/sqldiff.html)

というわけで、今回はSQLite sqldiffの使い勝手、およびPythonでsqldiffを利用する方法についてまとめたいと思います。


### ダウンロード

早速、下記からダウンロードします。

[SQLite Download](https://www.sqlite.org/download.html)

![main_window](../picture/SQLiteDownload.PNG)

Windows 10 (64bit)を使っているのですが、sqlite-tools-win32-x86-3280000.zip(1.70 MiB)しか無いですね。
本当に使えるのか？ 疑いがありましたが、結果から言いますと、動作してくれました。

ダウンロード後、zipファイルを展開し、任意のディレクトリにexeファイルらを置きます。

私は、C:\Program Files (x86) に 「sqlite-toolsフォルダ」を作成し、ここにexeファイルを格納しました。

では手始めに、コマンドプロンプトで実行してみました。

ここのスクリーンショットは割愛！
(きちんと動いているっぽいよ！！)


次に、Pythonのsubprocessライブラリ(標準ライブラリ)を使って先ほどコマンドプロンプト上で実行したことをPythonスクリプトで記述します。

以下の記事がとても参考になりました。

[Pythonのsubprocessで標準出力を取得](https://blog.imind.jp/entry/2019/02/17/012210)

### ソースコード
ということで、結論です。
以下のようなスクリプトを作成しました。

```InsertPicturesInDocument.py
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 13:25:33 2019
Spyderエディタ
For Python 3.7
@author: netchira
"""

def ExecSqldiff(db1, db2):
    import subprocess
    sqldiff_exe_path = r'C:\Program Files (x86)\sqlite-tools\sqldiff.exe'
    cmd = sqldiff_exe_path+' '+ db1 +' '+db2
    #cmd = [sqldiff_exe_path, db1, db2] # これでも動作する
    returncode = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    for line in returncode.stdout:
        print(line)

```

db1, db2を与えてあげると、差分についてsqldiffが教えてくれました。

### 感想
とりあえず満足しました。
もう少しSQLiteについて勉強していくぞ。

以上です。
