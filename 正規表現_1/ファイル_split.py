import re as 正規表現

def anal_スプリット(SPLIT, TXT):
	txt = TXT
	x = 正規表現.split(SPLIT, txt) # \s means white-spave
	print(x)


