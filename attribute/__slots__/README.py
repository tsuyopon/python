# 概要
__slots__を利用することで次の２点でメリットがあります。

- (1) メモリを節約することができます。
- (2) 誤った代入を未然に防ぐことができるようになる。

(1)については、Pythonではデフォルトではオブジェクトの属性はdictを使って保存しています。
この保存の仕方としては、実行中に動的に新たな属性を加えたりすることができますが、その利便性とは反対に誤った代入を防ぐことができなくなります。
予め属性などが動的に確保されないことがわかっているのであれば、__slots__を定義しておいたほうが賢明でしょう。

# 詳細

Good.pyとNotGood.pyという２つのサンプルを用意していますので、vimdiffなどで違いを確認してから実行してみてください。

NotGood.pyは本来trueと出力したかったが、誤った変数へセットしてしまったのでそこにセットされずにfalseとなっています。
```
$ python NotGood.py 
False
False
```

isSuccessを__slots__へとセットすることで、誤った変数へとセットすることでエラーを引き起こしてくれるようになります。
```
$ python Good.py 
False
Traceback (most recent call last):
  File "Good.py", line 15, in <module>
    t.setSuccess();
  File "Good.py", line 8, in setSuccess
    self.isSuccccccess = True;
AttributeError: 'Test' object has no attribute 'isSuccccccess'
```

# 参考URL
- qiita: ``__slots__``を使ってメモリを節約
  - https://qiita.com/tma15/items/1d7fbc4d56ac4b3678e1
- Pythonで__slots__を使う
  - http://welovy.hatenablog.com/entry/2012/11/20/005618
