import requests
import pandas as pd


def get_latest_trends(woeid):
	"""
	Takes in woeid of the location and returns "sorted" list of trends (hashtags) for that
	location, sort order: number of tweets for the hashtag, descending.
	NOTE: Trends are returned in list format with hashtags removed.
	"""
	bearer_token = ""

	# woeid India: 2282863

	endpoint = f"https://api.twitter.com/1.1/trends/place.json?id={woeid}"
	# data = {"ip": "1.1.2.3"}
	data = {}

	headers = {"Authorization": f"Bearer {bearer_token}"}

	result = requests.get(endpoint, data=data, headers=headers)
	res_json = result.json()
	df = pd.DataFrame(res_json[0]['trends']).sort_values("tweet_volume", ascending=False)
	trends_list = [x[1:] if x[0] == "#" else x for x in df['name'].to_list()]

	return trends_list


if __name__ == "__main__":
	result = get_latest_trends("2282863")
