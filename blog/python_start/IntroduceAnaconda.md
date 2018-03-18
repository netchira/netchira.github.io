---
layout: adv_book
titel:  Pythonを始めてみよう！(第1回:Anacondaを使ってみる)
description: Pythonの統合開発環境であるAnacondaを使ってみます。
lang: ja_JP
---
## Pythonを始めてみよう！(第1回:Anacondaを使ってみる)

以下のwebページから Anaconda をダウンロードできます。
ここからPythonをはじめてみましょう。

[Anaconda Download](https://www.anaconda.com/download/)

Pythonを始める上でまず初めに知っておくべきこと(個人的意見)をまとめてみました。

1. Anacondaで使うPythonのバージョンは、2.7 または 最新(3.x)のどちらかを選択すべし。
2. Python 2.x と Python 3.x で互換性がないと認識すべし。(微妙にライブラリ名が異なる。ソースコードをそのまま流用できることが少ない。)
3. Anaconda Navigator から、Spyderを起動し、ここでソースコードの実行・デバッグを行うべし。
4. 必要なライブラリは、Anaconda Promptのpipでインストールすることができるが、Anaconda Navigatorで行うべし。(Anaconda Navigatorでは、インストールしているライブラリを確認できる。)
5. (Open Sourceであるせいか、)Anaconda Navigator, Spyder共に、起動にすごく時間がかかる。じっくり待つべし。
6. Pythonの複数のバージョンを使用したい場合、「仮想環境」をつくると両バージョンをAnacondaで使えるようになる。
7. Pythonはとても人気のあるプログラミング言語なので、ググってみると知識がたくさんある。しかし、その分、間違った知識や、自分の環境には適さない情報なども混同しがち。


### Python：豊富なライブラリ群
まだ私もPythonを勉強し始めたところなのですが、<br>
numpy<br>
scipy<br>
matplotlib<br>
pandas<br>
この辺りのライブラリはコーディングするうえで有効かと思われます。
numpyは行列を用いた演算を高速で処理できるそうです。(まだ自分は使いこなせない)

まあ全てを理解しないとPythonは使えない、というわけではないと思います。
Python始めてみると、色んなことができることが分かってきて、けっこう楽しくなってきますよ。

また、PythonでGUIアプリケーションを作りたいならこの辺りが利用可能かと思います。参考情報です。

|Python2.7系|Python3.x系|ライブラリの概要|
|---|---|---|
|Tkinter|tkinter|GUIコントロール|
|ttk|tkinter.ttk|GUIコントロール(Comboboxが使える)|
|tkFileDialog|tkinter.filedialog|ファイル操作|
|tkMessageBox|tkinter.messagebox|メッセージボックス表示|

ちなみに、Anaconda/Spyderはこんな感じです。

Anaconda Navigator



Anaconda Prompt



Spyder




さあ、皆さんもPythonをはじめてみませんか！？
