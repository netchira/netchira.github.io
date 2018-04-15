---
layout: adv_book_html
title: GitHub Pages を作成する時のデバッグ作業の仕方
description: GitHub Pages を作成する時のデバッグ作業の仕方
lang: ja_JP
---
## GitHub Pages を作成する時のデバッグ作業の仕方

こんにちは、netchiraです。

今回のテーマは「GitHub Pagesでブログを作成する時のデバッグ作業の仕方」です。

「ブログをデバッグ」ってかなり変な言葉かもしれませんね。笑

というのも、GitHub Pages & Jekyll でwebページを作成できるので、
色々と記事を書こうと思い始めたところ、
「いちいち GitHub 上で Commit & Push しないとWebページが見れない」のが
とても面倒だなーと思うようになりました。

特に、SEO対策について今なお勉強中なのですが、
- jekyllの文法がわからん
- jekyll-seo-tagってどうやって使うん？
- 実際にできたHTMLのソースを見て、「うん？思うようになっていない。。。」

・・・といった壁にぶち当たっている訳です。

jekyllで生成するwebページをローカル(自分のPC上)で生成できる方法があることは
GithubPages本家のwebページを見てて、こういうのがあります。

[Setting up your GitHub Pages site locally with Jekyll](https://help.github.com/articles/setting-up-your-github-pages-site-locally-with-jekyll/)

ここでは、Rubyをインストールして、ごちゃごちゃすればできる、と書いているのですが、
かなりコストが高かったです。笑

ここでは試行錯誤の末、最終的に成功した方法だけを記しておきます。

以下、GitHub本家の[Setting up your GitHub Pages site locally with Jekyll]で紹介されている
手順に従って記述していきます。

**その前に1言だけ！！**

下記のサイトは大変役に立ちます。よかったらここも軽く目を通してから、この先をお読みください。  
[Johannes Peter氏のブログ](http://blog.johannesmp.com/2017/02/13/fixing-jekyll-serve-on-windows/)
1. Install all Jekyll Dependencies すべて  
2. Get Jekyll Server Working  
 Fix SSL “certificate verify failed”  
 Fix “No repo name found”  
 Fix “The GitHub API credentials you provided aren’t valid.”  

**では本題に移ります！！**

### Requirements
1. [RubyInstaller for Windows](https://rubyinstaller.org/downloads/)に行く。
2. RubyInstallers: Ruby 2.3.3 をダウンロードする。
そしてインストールする。
指定するオプションは次の2つ。
Rubyの実行ファイルへ環境変数PATHを設定する
.rbと.rbwファイルをRubyに関連付ける にチェックを入れてインストール
(こちらは簡単ですね。)

3. DEVEROMENT KIT : For use with Ruby 2.0 to 2.3 をダウンロードする。
ダウンロードしたファイルは、下記ディレクトリを作成して起き、ここに置く。
C:\RubyDevKit

4. DEVEROMENT KIT はRubyコマンドライン上で初期設定する。Git Bashを起動して行う。
```
$ cd C:\RubyDevKit
$ ruby dk.rb init
$ ruby dk.rb install
```
5. Bundler をインストールする。
```
$ gem install bundler
```

### Step 1
masterブランチでGithubPagesを作成していくので、何もしなくてよい。

### Step 2
1. ファイル名「Gemfile(拡張子：無し)」を作成する。
(右クリック→新規作成→テキスト ドキュメントから.txtファイルを作成して、拡張子を消して保存)
(※ファイルの拡張子が表示されない場合は、「拡張子の表示方法」とググってみてください。)
2. Gemfile の内容はたった2行だけ。
```
source 'https://rubygems.org'
gem 'github-pages', group: :jekyll_plugins
```

※ちなみに、ビルド時に下記のようにワーニングが出ますが、
下記1行は不要です。含めるとビルドできなくなります。
```
gem 'wdm', '>= 0.1.0' if Gem.win_platform?
```

3. Jekyll の更新を行う。
```
$ bundle install
```

### Step 3
何もしなくてよい。

### Step 4
1. いよいよJekyllでのwebページ生成です。初めにコマンドライン上で、
{ユーザー名}.github.io のディレクトリまでcdします。
2. 以下を実行します。
```
$ bundle exec jekyll serve
```
3. しかし、うまくいきません。残念！
そこで、下記のページを参考にしながら対策を実施していきます。
- _config.ymlファイルに「repository: (ユーザー名)/(リポジトリ名)」を1行追加する。
- [http://curl.haxx.se/ca/cacert.pem](http://curl.haxx.se/ca/cacert.pem) からSSL証明書をダウンロードしてくる。
- ダウンロードした`cacert.pem`を C:\RubyDevKit\SSLCert に置く。
- その後、環境変数=SSL_CERT_FILE を追加し、値=さっきのディレクトリ を設定します。
[環境変数の編集方法(参考)](https://support.borndigital.co.jp/hc/ja/articles/115010667707-環境変数の追加する方法について-Windows10-)
- GitHub API 用の認証が必要となるため、アクセストークンを [https://github.com/settings/tokens](https://github.com/settings/tokens) で取得する。
- その後、環境変数=JEKYLL_GITHUB_TOKEN を追加し、値=(40文字の英数字の羅列) を設定します。

4. 一度、コマンドライン上で`exit`と打ち込み、Git Bash の画面を閉じます。(上記の作業でRubyが必要とする情報が更新されたので、一旦リセット。)
5. 以下を再び実行します。
```
$ bundle exec jekyll serve
```
ワーニング及びエラーが出なくなったと思います。
6. ブラウザで下記のように入力。
```
http://127.0.0.1:4000
```
すると、ここでwebページの出来映えが確認できます。
7. `Ctrl + C` で ローカル上でのJekyllの動作を止めます。

これで、いちいち Commit & Push しなくても、webページの出来映え閣員ができる環境が構築できました。



### 以後のデバッグ作業では
1. {ユーザー名}.github.io のディレクトリまでcdします。
2. コマンドライン上で以下を実行します。
```
$ bundle exec jekyll serve
```

### ぼやき
今更なのですが、Jekyll のビルドは、生成するHTMLが10個にも満たないのに、
8-10秒くらいかかります。意外と時間かかりますね。仕方ないか。

あと、余談ですが、マークダウンで記述されたファイルをJekyllでHTML生成する場合は、
paginationが使えないらしいです。使ってみたかったなあ・・・

[https://jekyllrb.com/docs/pagination/](https://jekyllrb.com/docs/pagination/)
