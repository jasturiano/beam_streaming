import pymongo

"""

Code to query the latest document of the 'tweets' collection in MongoDB

"""

client = pymongo.MongoClient('mongodb://user:password@localhost:27017/')
db = client["corona_data"]
collection = db["tweets"]
document = collection.find_one()
##print(document)

latest_document = collection.find().sort("timestamp", pymongo.DESCENDING).limit(1)



for document in latest_document:
    print(document)





