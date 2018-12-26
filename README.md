# NST開発合宿事前勉強用競技プログラミング 回答チェッカー

## 概要
[NST開発合宿事前勉強用競技プログラミング](https://github.com/tetsuya-zama/devcamp-compe)の回答採点用Dockerイメージ

## ビルド

```bash
$ git clone https://github.com/tetsuya-zama/devcamp-compe-checker.git
$ cd devcamp-compe-checker
$ docker build -t devcamp-compe:latest .
```

## 採点実行

```bash
$ QUESTION=q1 # 問題番号(q1/q2/q3)
$ LANG=java # 言語(java/python/node)
# 採点対象のソースをローカルからボリュームマウントして実行
#  => $(pwd)/src配下に/[java8 | node8 | python3 ]/[Main.java | main.js | main.py ]がある状態で実行する
$ docker run --rm -v $(pwd)/src:/tmp/work/target devcamp-compe python /tmp/work/checker.py $QUESTION $LANG
```