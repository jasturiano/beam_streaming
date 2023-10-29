import apache_beam as beam
import time
import pymongo
import logging
from datetime import datetime

from .get_corona_cases import get_corona_cases

"""
    A ParDo transform that processes and stores incoming data in a MongoDB collection.

    This class establishes a MongoDB client, connects to a database and collection, and stores processed data.

"""

class ProcessAndStoreMessages(beam.DoFn):
    
    def setup(self):
       
        # Establish a MongoDB client and connect to the database and collection
        self.client = pymongo.MongoClient('mongodb://user:password@localhost:27017/')
        self.db = self.client["corona_data"]
        self.collection = self.db["tweets"]
 

    def process(self, element):
        
        content = element[1]

        total_case_count = get_corona_cases()
        timestamp = time.time()
        timestamp_datetime = datetime.fromtimestamp(timestamp)

        #Format the timestamp that will be stored in MongoDB
        timestamp_formatted = timestamp_datetime.strftime('%Y-%m-%d %H:%M:%S')


        data_to_store = {
            "content": content,
            "timestamp": timestamp_formatted,
            "total_case_count": total_case_count
        }

        try:
            self.collection.insert_one(data_to_store)
        except Exception as e:
            print(f"Error inserting data into MongoDB: {e}")

       
        