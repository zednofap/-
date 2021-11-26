import re as 正規表現

txt = "Hanimes with reverse r is good"

def anal_サブ():
	x = 正規表現.sub("\s", "ugh", txt) # \s means white-space
	print(x) # replaces the white-spaces with specific characters