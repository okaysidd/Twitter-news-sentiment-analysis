import datetime


def cache_trends(trends, woeid):
	path = "C:\\Users\\siddhartha.s\\Desktop\\something\\02. py_algo_ds\\THP\\cache\\"
	
	date = datetime.datetime.now()
	day = "0" + str(date.day)
	month = "0" + str(date.month)
	year = str(date.year)
	t_stamp = day[-2:] + month[-2:] + str(year)
	
	with open(f"{path}trends_{woeid}_{t_stamp}.txt", 'w') as f:
		for item in trends:
			try:
				f.write("%s\n" % item)
			except Exception as ex:
				print(f"Could not write {item} to file.")
				print(ex)
