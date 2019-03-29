このディレクトリ内にCoNLL-2003のeng.train, eng.testa, eng.testbを置いてください
データの入手法は以下の通り

# データの入手方法
## 正式な入手法
1. [CoNLL-2003公式サイト](https://www.clips.uantwerpen.be/conll2003/ner/)のner.tgzをダウンロード、展開
2. [Reuters](https://trec.nist.gov/data/reuters/reuters.html)の指示に従いrcv1.tar.xzを入手
3. 000READMEファイルに従ってeng.train、eng.testa、eng.testbを生成
4. data/ ディレクトリにeng.train、eng.testa、eng.testbを移動

## グレーな入手法
- [CodaLab](https://worksheets.codalab.org/bundles/0x1555644dcd6e42df8220676cb4d2b819/)などからrcv1.tar.xzを入手、上記方法に則って各種ファイル生成
- Githubで公開されているモデルのデータセット部分からeng.train、eng.testa、eng.testbを入手
    - ex. [Lample](https://github.com/glample/tagger)

# データ説明
- コーパス: Reuters通信の1393の英語ニュース記事
- データ:
    - 1行に単語、品詞タグ、チャンクタグ、NERタグの順にスペース区切り
    - 「-DOCSTART-」で1つ1つの文書が区切られている
    - 文章は空行で区切られている
- タグ:
    - NERタグ: 人名（PER）、地名（LOC）、組織名（ORG）、その他の名称（MISC）
    - IOBタグ: 二つの同名のNERタグが連続する場合B-XXXと表現、それ以外のNERタグはI-XXX、 Named entity以外はO
- eng.train: 学習データ(train)
- eng.testa: 検証データ(validation)
- eng.testb: 評価データ(test)