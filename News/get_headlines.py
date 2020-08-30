import requests
import pandas as pd


def get_headlines(searchTerm, country):
	"""
	Takes in searchTerm and returns list of tweets for that searchTerm.
	"""
	# endpoint = f"https://newsapi.org/v2/top-headlines?q={searchTerm}&apiKey={api_key}"
	# endpoint = f"https://newsapi.org/v2/top-headlines?country={country}&q={searchTerm}&apiKey={api_key}"
	
	api_key = ""
	endpoint = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}"
	headers = {}
	data = {}
	result = requests.get(endpoint, data=data, headers=headers)
	articles = result.json()['articles']

	headlines = [x['title'] for x in articles]

	return headlines


if __name__ == "__main__":
	result = get_headlines("Apple", "in")
