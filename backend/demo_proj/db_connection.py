import pymongo

url = 'mongodb://localhost:27017'
client = pymongo.MongoClient(url)

db = client['django_demo']
employees_collection = db['employees']
counter_collection = db['counters']