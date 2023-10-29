import apache_beam as beam
import requests
import logging

from apache_beam.options.pipeline_options import PipelineOptions, StandardOptions, WorkerOptions
from apache_beam.transforms.window import FixedWindows

from utils.pull_tweets import FetchDataFromFlask
from utils.store_messages import ProcessAndStoreMessages
from utils.clean_tweets import CleanTweets



ENDPOINT_URL = 'http://localhost:5555/stream'

#Dataflow pipeline options for Workers and Streaming configuration
pipeline_options = PipelineOptions()
pipeline_options.view_as(StandardOptions).streaming = True
worker_options = pipeline_options.view_as(WorkerOptions)
worker_options.max_num_workers = 1


def run_pipeline():
    

    with beam.Pipeline(options=pipeline_options) as pipeline:
            data = (
                pipeline
                | "StartPipeline" >> beam.Create([ENDPOINT_URL])
                
                | "ReadFromEndpoint" >> beam.ParDo(FetchDataFromFlask.get_messages_from_flask, ENDPOINT_URL)
                
                | "CleanData" >> beam.ParDo(CleanTweets())
                
                | "FixedWindows" >> beam.WindowInto(beam.window.FixedWindows(20))
                #| 'Keys' >> beam.Keys()
                
                | "GroupTweets" >> beam.GroupByKey()
                #| "LogElements" >> beam.LogElements() #For debugging purposes.
                
            )

            insert_mongodb = (
                data
                | "InsertMongoDB" >> beam.ParDo(ProcessAndStoreMessages())

            )
            
    
if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)
    print("Starting****")
    run_pipeline()
