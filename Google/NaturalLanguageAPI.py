# Set environment variable: GOOGLE_APPLICATION_CREDENTIALS=[PATH TO key.json]
from google.cloud import language
from google.cloud.language import enums, types


class NaturalLanguageAPI:

	def analyze_text_sentiment(self, text):
		"""
		text: text to do sentiment analysis for
		returns dictionary with text, score and magnitude
		"""
		client = language.LanguageServiceClient()
		document = types.Document(
			content=text,
			type=enums.Document.Type.PLAIN_TEXT)

		response = client.analyze_sentiment(document=document)

		sentiment = response.document_sentiment
		results = [
			('text', text),
			('score', sentiment.score),
			('magnitude', sentiment.magnitude),
		]
		# return results
		# for k, v in results:
		#     print('{:10}: {}'.format(k, v))
		
		# res = analyze_text_sentiment(text)
		
		results = {x[0]:x[1] for x in results}
			
		return results


if __name__ == "__main__":
	texts = [
		"Dalit man says filmmaker Nutan Naidu tonsured his head, case filed",
		"Sports Minister announces massive hike in prize money of National Sports Awards",
		"Sushant Singh Rajput death: Questions CBI is asking Rhea Chakraborty today",
		"RIP Chadwick Boseman: Avengers assemble to say goodbye to King T'Challa",
		"Seasonal torrential rains claim 125 lives in Pakistan: NDMA",
		"Coronavirus: In phase 2 of sero-survey, 1,500 samples to be collected in Odisha's Bhubaneswar",
		"I am going to kill you",
		"Kannada actor Vinayak Joshi marries Varsha Belawadi in lockdown",
		"RCB skipper Virat Kohli thrilled after first outdoor net session ahead of IPL 2020",
		"Flood-like situation in four Chattisgarh districts, thousands shifted"
	]

	obj = NaturalLanguageAPI()

	for text in texts:
		results = obj.analyze_text_sentiment(text)
		print(text)
		if results['score'] > 0:
			print('Positive')
		elif results['score'] < 0:
			print('Negative')
		else:
			print('Neutral')
		print(results['score'], results['magnitude'])
		print()
