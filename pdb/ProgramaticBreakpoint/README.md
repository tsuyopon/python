# 概要
プログラム上にてある遷移を通ったらpdbが自動的に起動する仕組みを提供してくれています。

通常は、pdbを実行するためには次のように毎回モジュールを指定しなければなりませんがその必要ありません。
```
$ python -m pdb xxx.py
```

# 詳細

test.py中の停止させてい行に以下を入れます。
```
import pdb; pdb.set_trace()
```

あとはpythonスクリプトを実行してその行を取った際にブレークポイントが自動的に貼られます。
```
$ python test.py 
hello
> /home/tsuyoshi/git/python/pdb/ProgramaticBreakpoint/test.py(8)<module>()
-> print "pdb"
(Pdb) 
```
