import pandas

#read json file with multiple lines in pandas
def read_file(file_name):
    # Read the file and return the dataframe
    return pandas.read_json(file_name, lines=True)

def top10_tweets(tweets):
    # Get the top 10 hashtags
    print(tweets.sort_values(by='retweetCount', ascending=False).head(10))

def users_with_most_tweets(tweets):
    users = []
    for tweet in tweets:
        if tweet['user']['username'] not in users:
            users.append((tweet['user']['username'],0))
            
        else:
            users[users.index(tweet['user']['username'])][1] += 1
    
    print(users.sort_values(by=1, ascending=False).head(10))    



tweets = read_file('farmers-protest-tweets-2021-2-4.json')
users_with_most_tweets(tweets)