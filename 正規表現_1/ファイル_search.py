import re as 正規表現

txt = "Yandere gf punish makes me happy"

def anal_探す():
	x = 正規表現.search("\s", txt) # \s means white-spave
	print("First space character located at", x.start()) # detecs a space character position