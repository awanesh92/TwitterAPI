import sys
import tweepy

#get the secret fields from a file just like a property file maintained in realtime applications
#field names are hardcoded as only limited values are required in case of large field values we can create dictionary and store values in them
def set_token_from_file():
	with open('TwitterAPIdetails.txt') as f:
		line=f.readline()
		while line:
			if 'Key' in line:
				global consumerKey
				consumerKey = line.split('=')[1].strip()
			elif 'umerSecret' in line:
				global consumerSecret
				consumerSecret = line.split('=')[1].strip()
			elif 'accessToken' in line:
				global accessToken
				accessToken = line.split('=')[1].strip()
			elif 'SecretToken' in line:
				global accessTokenSecret
				accessTokenSecret = line.split('=')[1].strip()
			line = f.readline()

def main(woeid):

	#load the details from the file
	set_token_from_file()
	auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
	auth.set_access_token(accessToken, accessTokenSecret)
	api = tweepy.API(auth)
	trnds = api.trends_place(woeid)
	# woeid = 2295377
	l1 = api.trends_place(woeid)[0]
	ltrends = l1["trends"]
	
	# print("Location  = ",trnds)
	ltrends.sort(key=lambda x: (x["tweet_volume"] is None ,x["tweet_volume"]),reverse=False)
	for i in range(10):
		print(ltrends[i]["name"],ltrends[i]["tweet_volume"])

if __name__ == "__main__":
	try:
		woeid = input("Enter the woeid for getting the top 10 trends ")
		main(int(woeid))
	except (KeyboardInterrupt, SystemExit):
		raise
	except Exception as error:
		print(error)
	else:
		pass
	finally:
		sys.exit(0)