import apache_beam as beam
import logging
import re
import datetime

    """
    CleanTweets is a ParDo transform that processes elements (tweets) and performs the following operations:
    1. Removes hashtags from the tweet.
    2. Removes 'RT:' characters from the tweet.
    3. Removes URLs from the tweet.
    4. Converts the timestamp from a UNIX timestamp to be used in the Fixed Window
    
    Args:
        element (dict): The input element containing 'tweet' and 'timestamp' fields.

    Yields:
        beam.window.TimestampedValue: A TimestampedValue containing the cleaned tweet and its timestamp.
    """

class CleanTweets(beam.DoFn):

    def process(self, element):

        tweet = element['tweet']
        timestamp = element['timestamp']

        tweet = re.sub(r'#\w+', '', tweet)  # Remove hashtags
        tweet = re.sub(r'RT:', '', tweet)   # Remove 'RT:' characters
        tweet = re.sub(r'http\S+', '', tweet)  # Remove URLs

        timestamp_datetime = datetime.datetime.fromtimestamp(timestamp)
        timestamp_formatted = timestamp_datetime.strftime('%Y-%m-%d %H:%M:%S')

        # Create a TimestampedValue with the timestamp and the tweet to be used in the Fixed Window
        
        timestamped_element = beam.window.TimestampedValue((timestamp, tweet), timestamp)


        
        yield timestamped_element
        
        
    
