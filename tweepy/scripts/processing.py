import tweepy

api_key = 'HM6RvuZSXPa23UDc9zmqKYXZq'
api_key_secret = 'aWfEDaYdUv3HXrgBtzhRvUiAbKJAlUx7pD5V7bgQvLTvUzr1Hb'
access_token = '1496715621903618049-oZOlbyxTDpJqCUH67O5kue0domcsiP'
access_token_secret = 'ruKLYKaSRv9i9Jg44kL9OH6zwg4FZZKevipDe7BiOR4Ue'

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def createDataSet(sourceFile, destinationFile):
    import csv
    import time

    counter = 0
    raw = []

    with open(sourceFile, 'r') as csvfile:
        lineReader = csv.reader(csvfile, delimiter=',')
        next(lineReader)
        for row in lineReader:
            raw.append({"tweet_id": row[1]})
    
    sleepTime = 2
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

sourceFile = "/Users/danny/Documents/School/APS360/Project/tweepy/tweet_ids/real.csv"
destinationFile = "/Users/danny/Documents/School/APS360/Project/tweepy/tagged/real.csv"

result = createDataSet(sourceFile, destinationFile)