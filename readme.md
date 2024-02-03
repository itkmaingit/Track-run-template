# Overview

Track run用のテンプレートプログラムです。Linux上でのPythonでの実行を想定しています。デバッグとテストの2つの手法で進めることができます。

## ライブラリインストール

```
pip install [package_name] --break-system-packages
```

と打ちましょう。本当は仮想環境を作ったほうが良いのですが面倒なので。せいぜいrequestsなどをインストールするだけなので特に問題はないはずです。

```
pip freeze > requirements.txt
```

と打てばその内容がテキストファイルに書き込まれるので、それをTrack run上のrequirements.txtに入力しておきましょう。

## Debug

ブレークポイントを打ち、F5を押すことによりin.txtの内容が入力されます。ただし、本番環境における入力の受け取り方とは異なる場合があるので、その部分は適宜修正してください。

## Test

```:bash
sh run.sh
```

と入力することでresult.txtに結果が吐き出されます。F1 -> Compare With...でout.txtとの差分を取ることによってどこが間違っているかを確かめることができます。環境が```python3```, ```python```, ```py```の場合があると思いますが、それは適宜変更してください。

## 入力の受け取り方

[参考](https://qiita.com/S-R-Programming/items/421322aaf1af3de4c51a)

基本的に、以下のコードで受け取ることができます。

```:python
def main(lines):

    for i, v in enumerate(lines):
        #print("line[{0}]: {1}".format(i, v))
        if(i==0): #1行目は数字の要素数 n
            n = v
        elif(i==1):
          a = list(map(int, v.split(" "))) #1行目じゃない(2行目)の時は数字のリストを取得
    print(n)
    print(a)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
```

入力例
```
3
3 1 5
```

出力例
```
3
[3, 1, 5]
```

のように、そもそもlinesには`["3", "3 1 5"]`というデータが保存されています。そのため、```for i, v in enumerate(lines):```の配下で、

- i行目で入力文字数が1つだけ（要素数など）のとき

```n=v```で受け取ることができます。適宜キャストを行う必要があります。

- i行目で入力文字数が複数ある場合

```a = list(map(int, v.split(" ")))```のように、`" "`半角スペースごとに区切ってリストに格納することができます。こちらはint型に変更しています。

行数ごとの分岐など、少し面倒になるかもしれませんが基本的にはこれで受け取れるはずです。