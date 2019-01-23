#!/usr/bin/python3

########################
# sort()
########################
# 通常のソート
sortlist = [5, 2, 3, 1, 4]
sortlist.sort()
print(sortlist)

########################
# sorted()
########################
# ディクショナリのソート
print(sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'}))

# 予め小文字に変換してから、文字列でリスト区切りにして、sortする。
print(sorted("This is a test string from Andrew".split(), key=str.lower))

# ２番めの要素x[1]をキーとしてソートする
dictionary = [['なら',3], ['かながわ',4], ['とうきょう',1], ['おおさか',2]]
sortedDict = sorted(dictionary, key=lambda x: x[1])
print(sortedDict)

# 3番目の要素をキーとしてソートする
student_tuples = [
	('john', 'A', 15),
	('jane', 'B', 12),
	('dave', 'B', 10),
]
print(sorted(student_tuples, key=lambda student: student[2]))

# 文字列のkeyをreplaceしてソートする
# 以下では、"hoge"の部分を意識せずに昇順ソートしたい。次のようにソートされるようにしたい
# [['ぐんま', '1.2.2_hoge3'], ['かながわ', '1.2.3'], ['なら', '1.2.3_hoge1'], ['おおさか', '1.2.3_hoge2'], ['さいたま', '1.2.3_3'], ['とうきょう', '1.2.4'], ['ちば', '1.2.4_hoge1'], ['やまなし', '1.2.4_hoge2'], ['ふくしま', '1.2.4_3']]
dictionary = [['なら', "1.2.3_hoge1"], ['かながわ', '1.2.3'], ['とうきょう','1.2.4'], ['おおさか','1.2.3_hoge2'], ['さいたま', '1.2.3_3'], ['ぐんま', '1.2.2_hoge3'], ['やまなし', '1.2.4_hoge2'], ['ふくしま', '1.2.4_3'], ['ちば', '1.2.4_hoge1']]
sortedDict = sorted(dictionary, key=lambda x: x[1].replace('_hoge','_'))
print(sortedDict)
