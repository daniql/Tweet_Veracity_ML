import tweepy

api_key = 'api key here'
api_key_secret = 'api key secret here'
access_token = 'access token here'
access_token_secret = 'access token secret here'

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

def createDataSet(sourceFile, destinationFile):
    import csv

    raw = []

    with open(sourceFile, 'r') as csvfile:
        lineReader = csv.reader(csvfile, delimiter=',')
        next(lineReader)
        for row in lineReader:
            raw.append({"tweet_id": row[1]})
    
    partialDataSet = []

    for tweet in raw:
        try:
            tweetFetched = api.get_status(tweet["tweet_id"])
            print("Tweet fetched: " + tweetFetched.text)
            tweet["text"] = tweetFetched.text
            partialDataSet.append(tweet)

        except Exception as e:
            print(e)
            continue
    
    with open(destinationFile, 'w') as csvfile:
        linewriter = csv.writer(csvfile, delimiter=',')
        for tweet in partialDataSet:
            try:
                linewriter.writerow([tweet["text"], '1'])
            except Exception as e:
                print(e)
    
    return partialDataSet

sourceFile = "where the file is for you"
destinationFile = "where you want to save the file"

result = createDataSet(sourceFile, destinationFile)