import tweepy

api_key = 'AVbXecczZ8bss5mHJGWhoZfd2'
api_key_secret = 'cTLpvDieSzZPvaaNkhXOQG3nMUln46ycQtEfaYsdSIKSlhF03S'
access_token = '1496715621903618049-g97Xa04OccWl07ernK7b0IsAzk5Eku'
access_token_secret = 'oV3s9zwI1yqJOY6eBWdyvGFQ2EHSf5vr0ry7SrdI0LWo0'

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

sourceFile = "/Users/danny/Documents/School/APS360/Project/tweepy/to_process/xab"
destinationFile = "/Users/danny/Documents/School/APS360/Project/tweepy/processed/xab.csv"

result = createDataSet(sourceFile, destinationFile)