# 概要
実行中のプロセスに対してpdbでプロセスアタッチをする方法について
pdbの現状の機能として稼働しているプログラムに対するアタッチの機能は存在しないが、シグナル制御をつかって同等のことができる。


# 詳細
test.pyにループするサンプルプログラムがあります。 実行するとその時のPIDを出力してくれます。
このプログラムはシグナルを受け取ると「import pdb; pdb.set_trace()」を実行します(詳しくはProgramaticBreakpoint)。
```
$ python test.py 
26955
```

先程のプログラムで出力されたpidに対してSIGUSR1を送ってみます。
```
$ kill -SIGUSR1 26955
```

シグナルをプログラム側が受信するとスクリプト側がPdb操作モードに切り替わります。
```
$ python test.py 
26955
> /home/tsuyoshi/git/python/pdb/ProcessAttach/test.py(14)loop()
-> while True:
(Pdb)
```

あとはpdbをインテラクティブに操作することができるようになります。
```
(Pdb) list
  9  	def handle_pdb(sig, frame):
 10  	    import pdb
 11  	    pdb.Pdb().set_trace(frame)    
 12  	
 13  	def loop():
 14  ->	    while True:
 15  	        x = 'foo'
 16  	        time.sleep(0.2)
 17  	
 18  	if __name__ == '__main__':
 19  	    signal.signal(signal.SIGUSR1, handle_pdb)
(Pdb)
```

# 参考
- https://stackoverflow.com/questions/25308847/attaching-a-process-with-pdb
