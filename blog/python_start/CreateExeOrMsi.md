---
layout: default
titel:  Pythonを始めてみよう！(第2回:exeファイル・msiファイルを生成する)
description: Pythonで作成したアプリケーションをWindows上で実行できるようにします。
lang: ja_JP
---
## Pythonを始めてみよう！(第2回:exeファイル・msiファイルを生成する)

こんにちは、netchiraです。
今回はPythonで作ったアプリケーションをPCで使えるようにしたいと思います。

### 前提条件
OS はWindows 10(64bit)を使用
Python 2.7 を使用
開発環境として Anaconda2(64bit) および Spyderを使用
py2exe(64bit, Python 2.7)を使用
cx_Freeze(64bit, Python 2.7)を使用

### Pythonアプリケーションの実行の仕方を検討

主な方法として、以下の2通りを検討していきます。

- .exeファイルを作成して、それを実行する。
- PCにインストールして、それを実行する。

Spyderで実行(及びデバッグ)できることは当然なので、今回はSpyderをインストールしていないPCでも実行できるようにしていきたいと思います。

下記に方法を記述していきます。


Attention：なお、下記の方法以外にも実現方法はあると思いますが、自分が気に入った方法だけを備忘録がてら記述していますので、読者の方はそのつもりでご一読ください。

### exeファイルの作り方
py2exeを使い、exeファイルの生成を行います。

初めにpy2exeをPCにインストールします。

[py2exeダウンロード先](https://sourceforge.net/projects/py2exe/files/py2exe/0.6.9/)

留意点：PCにインストールしているPythonが32bit/64bitのどちらかによって、インストールするpy2exeのバージョンが決まるそうです。

さて、次にやることは、exeを作るためのセットアップファイル(.py)の作成です。
一般的には'setup.py'というファイル名で作成します。

私は以下のようなsetup_exe.pyを書きました。

```setup_exe.py
from distutils.core import setup
import py2exe

script = 'CompareTxt.py'
option = {
    'compressed': 1,
    'optimize': 2,
    'bundle_files': 3,
}

setup(
    options = {
        'py2exe': option,
    },
    console = [
        {'script': script }
    ],
    zipfile = None,
)
```

このsetup_exe.pyは、今回exe化したいpythonファイル(CompareTxt.py)と同じ場所に置きます。

なお、色んな方がセットアップファイル(setup.py)を書いているので、ググってみると参考になると思います。

さて、ここまでくると、ようやくexeファイル生成が実行できるようになります。
以下の2つの手順で完了です。

1. Anaconda Prompt で'exeファイルにしたいpyファイル'および'setup_exe.py'が格納されているフォルダまでcd(change directory)していきます。
```
cd HogeHogeHoge/HogaHogaHoga
```

2. 次に以下を実行します。
```
python setup_exe.py py2exe
```
⇒すると、先ほどcdした場所に/distというフォルダが出来て、その中に、見事exeファイルができています！やったね！

### 余談その1:dllのしがらみ
以前、生成したexeファイルだけを別のPCで実行しようとしたのですが、アプリケーション実行時に必要なdllがないと動作できないようで、「exeファイルにしたいpyファイルでimportしているライブラリ」のdllが重要っぽいです。つまり、/distフォルダごと別PCに移さないと実行できません、ということでした。

### 余談その2:optionについて
py2exeのoptionって何を表しているのでしょう。
答えは以下に記載されています。

[py2exe](http://www.py2exe.org/index.cgi/ListOfOptions)

### Windowで動作するインストーラの作り方
cx_Freezeを使い、msiファイルの生成を行います。

初めにcx_FreezeをPCにインストールします。

[cx_Freezeダウンロード先](https://ja.osdn.net/projects/sfnet_cx-freeze/)

次にやることは、msiを作るためのセットアップファイル(.py)の作成です。
先ほどと区別するため、setup_msi.pyというファイル名にします。
こちらは、setup_exe.pyに比べてソースコードが長くなっているので、
詳しくはGitHub上の私のリポジトリを参照してください。

[GitHub/netchira/python](https://github.com/netchira/netchira.github.io/tree/master/python)
←ここが私のリポジトリです。

Anaconda コマンドプロンプトでmsiファイルにしたいpyファイルと、setup_msi.pyを格納しているフォルダまでcdしていきます。
次に以下を実行します。

```
python setup_msi.py bdist_msi
```

すると、先ほどcdした場所に/distというフォルダが出来て、その中に、見事msiファイルができています！やったね！


ちなみに`cx_Freeze Python exe`とかでググってみると色々出てきます。

また、私は今回セットアップ用のファイルをsetup_msi.pyと呼びましたが、
これは一般的ではないようです。setup.pyと呼ぶべきなのだとか。。。
(自分勝手なファイル名にしてます。スミマセン。)

### 余談その3：アイコンファイル(.ico)作成方法
ググったら一発なのですが、便利なサイトがあったので紹介します。

[.icoファイル生成サイト](https://ao-system.net/alphaicon/)

### 参考URL
[cx_Freeze公式サイト](http://cx-freeze.readthedocs.io/en/latest/distutils.html)

