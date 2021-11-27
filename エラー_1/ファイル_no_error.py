def anal_エラーなし(PRINT, NO_ERROR, ERROR, FINALLY):
	try:
		print(PRINT)
	except:
		print(ERROR)
	else:
		print(NO_ERROR)
	finally:
		print(FINALLY)