import pymongo
from pymongo import MongoClient

DATABASE_CLUSTER = MongoClient(
    "mongodb://admin:G6HyJikC1wKwoz1c@main-cluster-shard-00-00.hukmn.mongodb.net:27017,main-cluster-shard-00-01.hukmn.mongodb.net:27017,main-cluster-shard-00-02.hukmn.mongodb.net:27017/<dbname>?ssl=true&replicaSet=atlas-rct4tj-shard-0&authSource=admin&retryWrites=true&w=majority")

DATABASE = DATABASE_CLUSTER["travmedia"]

USERS_COLLECTION = DATABASE["users"]
POST_COLLECTION = DATABASE["posts"]

new_id = POST_COLLECTION.count() + 1
post = {"_id": new_id, "publisher": "Ruby", "title": "WOW", "content": "Hello class", "publishing_date": "10/02/2021, 11:28:31"}
POST_COLLECTION.insert_one(post)

all_posts = mongo_cursor_result = POST_COLLECTION.find({})
for item in all_posts:
    print(item)

print(f"Found: {USERS_COLLECTION.find_one({'username': 'rudovruben'})}")
