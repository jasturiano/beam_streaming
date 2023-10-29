import requests
import json
import apache_beam as beam
from datetime import datetime


"""
    A ParDo transform that fetches and processes streaming data from a Flask server.

    Args:
        endpoint_url (str): The URL of the Flask server endpoint to fetch data from.

    Yields:
        dict: A dictionary containing the fetched tweet and its timestamp.
"""

class FetchDataFromFlask(beam.DoFn):
    def get_messages_from_flask(self, endpoint_url):
        
        response = requests.get(endpoint_url, stream=True)
        
        for line in response.iter_lines():
            if line:
                message = json.loads(line.decode('utf-8'))
                if "data" in message:
                    tweet = message["data"]
                    current_time = int(datetime.now().timestamp())
                    tweet_with_timestamp = {'tweet': tweet,'timestamp': current_time}
                    yield tweet_with_timestamp