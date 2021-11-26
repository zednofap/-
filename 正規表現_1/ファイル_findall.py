import re as 正規表現

txt = "Hanime, Hen, Hanime, Hanime"

def anal_すべて検索():
	x = 正規表現.findall("an", txt) # detect "an" letters
	print(x)