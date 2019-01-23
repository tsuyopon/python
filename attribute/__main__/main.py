print("start program");

def main():
	print("start main")


# __main__はmain文ですが、以下のようなおまじない的な記述をします。
# 以下の記述はimport時に、勝手にmain処理を実行しないようにするための記述です。
# なお、import時には動作しませんが、"python main.py"と実行された場合にはこのif文は処理されます。
if __name__ == "__main__":
	print("start __main__")
	main()
