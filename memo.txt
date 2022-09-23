# MeCab in Ubuntu-20.04
## システム辞書を再コンパイルする方法
- MeCabのインストール
  - https://qiita.com/ekzemplaro/items/c98c7f6698f130b55d53
- https://zenn.dev/suyaa/articles/4f525a16a016e3
  - こちらを採用
- mecabrcの場所
  - `python3-mecab`を利用する環境では`/usr/local/etc/mecabrc`を探しに行くが、存在しないので、シンボリックリンクを貼って解決する
  ```
  /usr/local/etc$ ln -s /etc/mecabrc mecabrc
  /usr/local/etc$ la
  mecabrc -> /etc/mecabrc
  ```
- 辞書の場所
  - [https://qiita.com/ekzemplaro/items/c98c7f6698f130b55d53](https://qiita.com/ekzemplaro/items/c98c7f6698f130b55d53)に従ってインストールすると、`/usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd`にインストールされるが、こちらはここでは使わない
  - [https://zenn.dev/suyaa/articles/4f525a16a016e3](https://zenn.dev/suyaa/articles/4f525a16a016e3)に従って進めていくと、`make install`したら、`/usr/lib/x86_64-linux-gnu/mecab/dic/ipadic`が生成されるので、`/etc/mecabrc`のシステム辞書の指し先をこちらにする
  ```
  ;
  ; Configuration file of MeCab
  ;
  ; $Id: mecabrc.in,v 1.3 2006/05/29 15:36:08 taku-ku Exp $;
  ;

  ; dicdir = /var/lib/mecab/dic/debian
  dicdir = /usr/lib/x86_64-linux-gnu/mecab/dic/ipadic
  ...
  ...
  ```
## 補足：システム辞書からユーザー辞書を指す方法
- https://zenn.dev/suyaa/articles/cb8a7e0c2767b3
  - ラストでエラーのため断念
    ```
    feature_index.cpp(158) [mmap_.open(modelfile.c_str())] mmap.h(152) [(fd = ::open(filename, flag | O_BINARY)) >= 0] open failed:
    ```
