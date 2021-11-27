import re as 正規表現

def anal_サブ(SEARCH, SUB, TXT):
	txt = TXT
	x = 正規表現.sub(SEARCH, SUB, txt) # \s means white-space
	print(x) # replaces the white-spaces with specific characters