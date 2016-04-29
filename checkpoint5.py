from pymongo import MongoClient
import random
import time
import datetime
client = MongoClient()


def random_word_requester():
	'''
	This function should return a random word and its definition and also
	log in the MongoDB database the timestamp that it was accessed.
	'''
	db = client.csci2963
	posts = db.definitions
	size = len(list(posts.find()))
	i = random.randint(0, size-1)
	word = list(posts.find())[i]["word"]
	timestamp = str(datetime.datetime.fromtimestamp(time.time()))
	posts.update({"word":word}, {"$push":{"dates":timestamp}})
	return str(list(posts.find())[i])


if __name__ == '__main__':
	print random_word_requester()
