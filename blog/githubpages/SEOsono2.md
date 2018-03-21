---
layout: adv_webdesign
title: GitHub Pages でのSEO対策について
description: GitHub Pages でのSEO対策について考察します
lang: ja_JP
---
## GitHub Pages でのSEO対策について

こんにちは、netchira です。

今回はGitHub Pages で作成したwebページのSEO対策について、何を実践していけばいいか個人的見解を紹介していきます。

- GitHub Pagesプラグインjekyll-seo-tagを使用
- とりあえず1ヶ月くらい待ってみる

### 前提条件
Google Search Console に自分のwebページを登録していること

### 参考資料
[ヘルプ: 検索エンジン最適化（SEO）スターター ガイド](https://support.google.com/webmasters/answer/7451184?hl=ja&ref_topic=3309469)

※以下、SEOスターターガイドと呼ぶこととします。

### プラグインjekyll-seo-tagでできること

このプラグインを’_config.yml’に記述しておくと、Googleが公開している「SEOスターターガイド」に記載されている以下のことができるようになります。

1. ページタイトル `<title>`タグを指定する
2. ページの概要 descriptionメタタグを指定する


### SEO対策その1: 固有の正確なページタイトルを付ける

SEOスターターガイドには以下のような記述があります。


` <title>タグはユーザーと検索エンジンの両方にページの内容を伝えるものです。<title>タグはHTMLドキュメントの <head>要素内に配置する必要があります。サイトの各ページに固有のタイトルを付けてください。`


まだ私も100%活用できている自信はありませんが、この`<title>`タグがGoogle検索でヒットする上で重要な要素の一つである、ということです。

オリジナリティの高い、且つ、内容がすぐに分かる`<title>`をつくって、Google検索に自分のwebページがヒットするようになることを目指したいものです。

### SEO対策その2: description メタタグを使用する

再び引用です。


`ページの description メタタグは Google や他の検索エンジンにページ内容の要約を伝えます。ページのタイトルが数語の単語やフレーズであるのに対し、ページの description メタタグには 1、2 文のセンテンスや短いパラグラフを記述します。`


こちらも、SEO対策に欠かせない要素である、とのこと。
内容が分かりやすい

ちなみに、これらの内容を書くのはマークダウンファイル(拡張子: .md, .markdown)の先頭です。

こんな感じで書きます。

```
---
layout: default
title: GitHub Pages でのSEO対策について
description: GitHub Pages でのSEO対策について考察します
lang: ja_JP
---
## GitHub Pages でのSEO対策について

こんにちは、netchira です。

(以下、略)
```

### とりあえず待ってみる
さて、いくつか方法を紹介してみましたが、「どうしても急がないといけない人」を除いて、しばらく待てる人は、ちょっと待ってみるのも良い方法かと思います。

SEO対策でググると色んな情報が出てきますし、なんだか迷ってしまいますよね。

なので、何かしら自分で試してみたのなら、まずは2,3日待ってみて、1,2週間待ってみて、、、さすがに1ヶ月たてば効果が出始めてもいいとは思いますが、そういう「気長さ」があっても良いのではないでしょうか。



以上です。

参考になれば幸いです。