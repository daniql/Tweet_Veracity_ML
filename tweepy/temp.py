import tweepy

api_key = 'chdJOsmGQaS4gqAPYpkiBzsIm'
api_key_secret = 'WHhuj5Z8vlw1mi6prckDbdFcWtCmWNIPP2wqBguHTV71OgOjOZ'
access_token = '2531610866-YTDqkzarilXx7UXdhfQRHBL11CAyTYWTonbZzON'
access_token_secret = 'EB6Pze8xeYIqnoAIZkZuKFXy2IuIYIIEKDTTE1VqIkhsg'

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

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

sourceFile = "/Users/danny/Documents/School/APS360/Project/tweepy/tweet_ids/real2.csv"
destinationFile = "/Users/danny/Documents/School/APS360/Project/tweepy/tagged/real2.csv"

result = createDataSet(sourceFile, destinationFile)