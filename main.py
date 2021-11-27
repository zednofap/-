from フォルダ_1.ファイル_classes import x as 知識_1
from 算数_1.ファイル_min_max import anal_最小最大 as 知識_2
from 算数_1.ファイル_abs import anal_絶対 as 知識_3
from 算数_1.ファイル_sqrt import anal_平方根 as 知識_4
from 算数_1.ファイル_ceil_floor import anal_天井階 as 知識_5
from 正規表現_1.ファイル_findall import anal_すべて検索 as 知識_6
from 正規表現_1.ファイル_search import anal_探す as 知識_7
from 正規表現_1.ファイル_split import anal_スプリット as 知識_8
from 正規表現_1.ファイル_sub import anal_サブ as 知識_9
from エラー_1.ファイル_error import anal_エラーがあります as 知識_10
from エラー_1.ファイル_no_error import anal_エラーなし as 知識_11
from 入力_1.ファイル_input import anal_入力 as 知識_12

# Required Config log
from 構成ログ import ファイル_CLASSES_X_NAME, ファイル_CLASSES_X_AGE, ファイル_ERROR, ファイル_NO_ERROR, ファイル_ERROR_PRINT, ファイル_FINALLY, ファイル_INPUT_EX, ファイル_INPUT, ファイル_FINDALL, ファイル_FINDALL_TXT, ファイル_SEARCH_TXT, ファイル_SEARCH, ファイル_SEARCH_PRINT, ファイル_SPLIT_TXT, ファイル_SPLIT, ファイル_SUB_TXT, ファイル_SUB_SEARCH, ファイル_SUB, ファイル_ABS, ファイル_CEIL, ファイル_FLOOR, ファイル_MIN_MAX, ファイル_SQRT

# inheritance, objects, classes
知識_1.印刷()
# math
知識_2(ファイル_MIN_MAX)
知識_3(ファイル_ABS)
知識_4(ファイル_SQRT)
知識_5(ファイル_CEIL, ファイル_FLOOR)
# regex
"""
\A	Returns a match if the specified characters are at the beginning of the string	"\AThe"	Try it »
\b	Returns a match where the specified characters are at the beginning or at the end of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\bain"
r"ain\b"	Try it »
Try it »
\B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\Bain"
r"ain\B"	Try it »
Try it »
\d	Returns a match where the string contains digits (numbers from 0-9)	"\d"	Try it »
\D	Returns a match where the string DOES NOT contain digits	"\D"	Try it »
\s	Returns a match where the string contains a white space character	"\s"	Try it »
\S	Returns a match where the string DOES NOT contain a white space character	"\S"	Try it »
\w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"	Try it »
\W	Returns a match where the string DOES NOT contain any word characters	"\W"	Try it »
\Z	Returns a match if the specified characters are at the end of the string
"""
知識_6(ファイル_FINDALL, ファイル_FINDALL_TXT)
知識_7(ファイル_SEARCH_PRINT, ファイル_SEARCH, ファイル_SEARCH_TXT)
知識_8(ファイル_SPLIT, ファイル_SPLIT_TXT)
知識_9(ファイル_SUB_SEARCH, ファイル_SUB, ファイル_SUB_TXT)
# errors
知識_10(ファイル_ERROR, ファイル_FINALLY)
知識_11(ファイル_ERROR_PRINT,ファイル_NO_ERROR, ファイル_ERROR, ファイル_FINALLY)
# input
知識_12(ファイル_INPUT_EX, ファイル_INPUT)