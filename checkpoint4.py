from pymongo import MongoClient
client = MongoClient()

if __name__ == '__main__':
   db = client.csci2963
   posts = db.definitions
   print posts.find()
   print posts.find_one() 
   print posts.find({"word": "Capitalandi"})
   print posts.find({"_id": "ObjectId('56fe9e22bad6b23cde07b8ce')"})
   post = {'definition': " exp. To laugh out loud.", 'word': 'lol'}
   posts.insert_one(post)
