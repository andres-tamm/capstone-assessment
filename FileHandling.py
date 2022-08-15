import pandas
import os



# Function to read the file and return the dataframe with pandas
def read_file(file_name):
    # Read the file and return the dataframe
    return pandas.read_json(file_name)

def top10_tweets(tweets):
    # Get the top 10 hashtags
    return tweets.sort_values(by='retweetCount', ascending=False).head(10)
