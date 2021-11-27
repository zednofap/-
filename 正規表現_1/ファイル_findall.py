import re as 正規表現

def anal_すべて検索(FINDALL, TXT):
	txt = TXT
	x = 正規表現.findall(FINDALL, txt) # detect "an" letters
	print(x)

