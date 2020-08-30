from Google import NaturalLanguageAPI
from Twitter import get_trends, get_tweets
from utilities.utilities import cache_trends
from News import get_headlines
import pandas as pd
import datetime
import os


def main():
	india_woeid = "2282863"
	woeid = india_woeid
	
	path = "C:\\Users\\siddhartha.s\\Desktop\\something\\02. py_algo_ds\\THP\\cache\\"
	files = os.listdir(path)
	
	date = datetime.datetime.now()
	day = "0" + str(date.day)
	month = "0" + str(date.month)
	year = str(date.year)
	t_stamp = day[-2:] + month[-2:] + str(year)
	file_prefix = f"trends_{woeid}_{t_stamp}.txt"
	files_with_prefix = [x for x in files if x.endswith(file_prefix)]
	
	if len(files_with_prefix) > 0:
		print(f"Reading trends for {t_stamp} from cache.")
		trends = []
		with open(path+files_with_prefix[0]) as file:
			for line in file: 
				line = line.strip() #or some other preprocessing
				trends.append(line) #storing everything in memory!
	else:
		print("No cache found at path, querying for new trends")
		trends = get_trends.get_latest_trends(woeid)
		cache_trends(trends, woeid)

	# tweets for trending topics
	tweets = {}
	for trend in trends[:5]:
		tweets[trend] = get_tweets.get_tweets(trend)
		
	results = {}
	sentiment_analysis = NaturalLanguageAPI.NaturalLanguageAPI()
	for key, value in tweets.items():
		for text in value:
			try:
				res = sentiment_analysis.analyze_text_sentiment(text)
				results[(key, text)] = (res['score'], res['magnitude'])
			except Exception as ex:
				# print(f"{text} from {key} could not be evaluated")
				# print(ex)
				pass

	# news headlines for trending topics
	country = "in"
	news_headlines = {}
	for trend in trends[:5]:
		news_headlines[trend] = get_headlines.get_headlines(trend, country)

	# sentiment_analysis = NaturalLanguageAPI.NaturalLanguageAPI()
	for key, value in news_headlines.items():
		for text in value:
			try:
				res = sentiment_analysis.analyze_text_sentiment(text)
				results[(key, text)] = (res['score'], res['magnitude'])
			except Exception as ex:
				# print(f"{text} from {key} could not be evaluated")
				# print(ex)
				pass

	df = pd.DataFrame(results).T
	df_pos = df[df[0]>0]
	df_neg = df[df[0]<0]

	pd.DataFrame(results).to_json("some.json")

	df_pos.to_csv("df_pos.csv", index=False)
	df_neg.to_csv("df_neg.csv", index=False)
	return df_pos

main()
