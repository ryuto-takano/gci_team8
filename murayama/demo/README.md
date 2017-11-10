## word2vecを使う

### 参考サイト
[Python で「老人と海」を word2vec する](https://m0t0k1ch1st0ry.com/blog/2016/08/28/word2vec/)

[MacOSとHomebrewとpyenvで快適python環境を。](https://qiita.com/crankcube@github/items/15f06b32ec56736fc43a)
[Macにnkfコマンドをインストールしてみる](http://kengo92i.hatenablog.jp/entry/2016/09/06/120854)
[Python3からMeCabを使う](https://qiita.com/taroc/items/b9afd914432da08dafc8)

### 環境設定をする
いろいろごちゃごちゃやったので最短ルートが不明。参考サイトがLinuxだったのでMac.verでやってみた。

- pyenvのインストール
`git clone https://github.com/yyuu/pyenv.git ~/.pyenv`

-MeCabとその辞書のインストール
Home brew が入ってなかったらインストールしましょう
`brew install mecab`
`brew install mecab-ipadic`

-mecab-ipadic-NEologd(新辞書)のインストール
`brew install git curl xz`
`git clone --depth 1 git@github.com:neologd/mecab-ipadic-neologd.git`

-nkfコマンドをインストールするためにx-codeをインストールしてmac port をインストールした。

これで[Python で「老人と海」を word2vec する](https://m0t0k1ch1st0ry.com/blog/2016/08/28/word2vec/)の実装ができるはず。
次は食べログ口コミ.txtを取ってこよう。

