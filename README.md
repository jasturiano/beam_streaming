## Streaming Data Processing with Apache Beam

**Description**: This project demonstrates a streaming data processing pipeline using Apache Beam, designed to read data from a streaming endpoint, clean and aggregate data scraping latest Corona cases, and store it in a MongoDB database.

## Prerequisites

Before running the code, make sure you have the following prerequisites installed:

    - Python
    - Apache Beam
    - MongoDB (with the required Python libraries)

You may also need to adjust the endpoint_url to the correct streaming data source. By default it's configured to localhost:5555

## Code Overview

The code consists of the following components:

  1.   Pipeline Configuration: It sets up the Apache Beam pipeline with streaming options, including specifying the streaming mode and the number of workers.

  2.   Data Ingestion: It uses the FetchDataFromFlask class to fetch data from a streaming endpoint (specified by endpoint_url).

  3.   Data Cleaning: The CleanTweets class processes the incoming data, removing hashtags, URLs, and other unwanted elements.

  4.   Windowing: The data is windowed into fixed 20-second windows using beam.WindowInto then grouped by the start time of each fixed window, using beam.GroupByKey.

  5. Data Storage: The ProcessAndStoreMessages class stores the grouped data into a MongoDB database including data from Corona latest cases scraping the info using beautifulsoup4.

Extras: The twitter_stream_simulator.py file demonstrates a basic Flask application that simulates streaming random tweets. The app generates random tweet-like messages and streams them over HTTP when a client  makes a GET request to the /stream endpoint.

Running the code
```bash
1. Start the Flask app
python twitter_stream_simulator

2. Run the apache Beam pipeline
python your_script_name.py
```

## TODO

Add a streaming processing framework such as PubSub or Kafka to add reliability and better control of the messages coming from twitter simulator (eventually a real time X/Twitter connection)

