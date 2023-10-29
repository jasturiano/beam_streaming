Streaming Data Processing with Apache Beam

This project demonstrates a streaming data processing pipeline using Apache Beam, designed to read data from a streaming endpoint, clean and aggregate data scraping latest Corona cases, and store it in a MongoDB database.

Prerequisites

Before running the code, make sure you have the following prerequisites installed:

    Python
    Apache Beam
    MongoDB (with the required Python libraries)

You may also need to adjust the endpoint_url to the correct streaming data source. By default it's configured to localhost:5555

Code Overview

The code consists of the following components:

    Pipeline Configuration: It sets up the Apache Beam pipeline with streaming options, including specifying the streaming mode and the number of workers.

    Data Ingestion: It uses the FetchDataFromFlask class to fetch data from a streaming endpoint (specified by endpoint_url).

    Data Cleaning: The CleanTweets class processes the incoming data, removing hashtags, URLs, and other unwanted elements.

    Windowing: The data is windowed into fixed 20-second windows using beam.WindowInto then grouped by the start time of each fixed window, using beam.GroupByKey.

    Data Storage: The ProcessAndStoreMessages class stores the grouped data into a MongoDB database including data from Corona latest cases scraping the info using beautifulsoup4.

    Extras: The twitter_stream_simulator.py file demonstrates a basic Flask application that simulates streaming random tweets. The app generates random tweet-like messages and streams them over HTTP when a client  makes a GET request to the /stream endpoint.

python your_script_name.py

Make sure to replace your_script_name.py with the actual name of your Python script.
Error Handling

The code contains a basic exception handling mechanism to catch and handle errors during data storage. You can further customize error handling to suit your requirements.
Additional Notes

    The code can be extended and customized to meet specific streaming data processing needs.
    Logging is enabled to provide information about the pipeline's progress.

This README provides an overview of the streaming data processing pipeline. Be sure to configure the MongoDB connection and other settings to align with your specific use case.
Free Research Preview. ChatGPT may produce inaccurate information about people, places, or facts. ChatGPT September 25 Version
