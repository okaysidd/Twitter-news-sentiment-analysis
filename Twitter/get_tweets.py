import requests
import pandas as pd


def get_tweets(searchTerm):
	"""
	Takes in searchTerm and returns list of tweets for that searchTerm.
	"""
	endpoint = f"https://api.twitter.com/2/tweets/search/recent?query={searchTerm}"
	bearer_token = ""
	headers = {"Authorization": f"Bearer {bearer_token}"}
	data = {}
	result = requests.get(endpoint, data=data, headers=headers)

	df = pd.DataFrame(result.json()['data'])

	tweets = df["text"].to_list()
	return tweets


if __name__ == "__main__":
	result = get_tweets("arsenal")
