import re as 正規表現

def anal_探す(PRINT, SEARCH, TXT):
	txt = TXT
	x = 正規表現.search(SEARCH, txt) # \s means white-spave
	print(PRINT, x.start()) # detecs a space character position

