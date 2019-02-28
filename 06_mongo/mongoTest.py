# Joan Chirinos
# SoftDev2 pd08
# K06 -- Yummy Mongo Py

# python package for MongoDB
# import pymongo

# import only the things we'll use?
from pymongo import MongoClient
# import pprint to print pretty JSON
from pprint import pprint

# connect to a mongo server
# adress should be string, port should be int
# default port = 27017
def connect(address, port=27017):
    client = MongoClient(address, port)
    return client

# get a database given a client and a db name
def getDatabase(client, name):
    # We could do this ONLY if name is a valid Python attribute name.
    # We can't guarantee it, so we use the dictionary-style syntax instead
    # db = client.name
    db = client[name]
    return db

# get a collection given the database and the collection name
def getCollection(db, name):
    # We could do this ONLY if name is a valid Python attribute name.
    # We can't guarantee it, so we use the dictionary-style syntax instead
    # collection = db.name
    collection = db[name]
    return collection

# inserts a document into a collection
# returns the document ID
# assumes the document is a dictionary structured like JSON
# assumes the document either has no ID (one will be created) OR a UNIQUE ID
def insertDocument(collection, document):
    id = collection.insert_one(document).inserted_id
    return id

# gets documents in collection which match the querydict (Python dictionary)
# returns an iterable of all documents found
def findDocuments(collection, queryDict):
    docs = collection.find(queryDict)
    return docs

# counts all documents, or all documents that match queryDict, in a collection
def countDocuments(collection, queryDict={}):
    return collection.count_documents(queryDict)

# TESTING METHOD #
def test():
    # connecting to my droplet (using the default port)
    client = connect('206.189.236.112')
    # get test DB from DO client
    db = getDatabase(client, 'test')
    # get restaurants collection from test DB
    restaurantsCollection = getCollection(db, 'restaurants')

    # (For each section, only printing first 3 documents)
    # Assignment: Get...

    # ...all restaurants in a specified borough (change index to change borough)
    borough = ['Bronx', 'Brooklyn', 'Queens', 'Manhattan', 'Staten Island'][0]
    boroughQuery = {'borough': borough}
    restaurantsInBorough = findDocuments(restaurantsCollection, boroughQuery)
    print('\n{0}\nRESTAURANTS WITH borough: |{1}|\n{0}'.format('='*40, borough))
    for i in range(3):
        try:
            pprint(restaurantsInBorough[i])
            print('\n')
        except:
            pass

    # ...all restaurants in a specified zip code
    zipcode = '10462'
    zipcodeQuery = {'address.zipcode': zipcode}
    restaurantsInZipcode = findDocuments(restaurantsCollection, zipcodeQuery)
    print('\n{0}\nRESTAURANTS WITH zipcode: |{1}|\n{0}'.format('='*40, zipcode))
    for i in range(3):
        try:
            pprint(restaurantsInZipcode[i])
            print('\n')
        except:
            pass

    # ...all restaurants in a specified zip code and with a specified grade.
    # (change index to change grade)
    zipcode = '10462'
    grade = ['A', 'B', 'C', 'D', 'F'][0]
    zipcodeGradeQuery = {'address.zipcode': zipcode, 'grades.grade': grade}
    restaurantsInZipcodeWithGrade = findDocuments(restaurantsCollection, zipcodeGradeQuery)
    print('\n{0}\nRESTAURANTS WITH zipcode: |{1}| WITH grade: |{2}|\n{0}'.format('='*40, zipcode, grade))
    for i in range(3):
        try:
            pprint(restaurantsInZipcodeWithGrade[i])
            print('\n')
        except:
            pass

    # ...all restaurants in a specified zip code with a score below a specified threshold.
    zipcode = '10462'
    maxScore = 20
    zipcodeMaxScoreQuery = {'address.zipcode': zipcode, 'grades.score': {'$lt': maxScore}}
    restaurantsInZipcodeWithMaxScore = findDocuments(restaurantsCollection, zipcodeMaxScoreQuery)
    print('\n{0}\nRESTAURANTS WITH zipcode: |{1}| AND maxScore: |{2}|\n{0}'.format('='*40, zipcode, maxScore))
    for i in range(3):
        try:
            pprint(restaurantsInZipcodeWithMaxScore[i])
            print('\n')
        except:
            pass

    # ...something more clever
    # --> stats on documents
    numberOfRestaurants = countDocuments(restaurantsCollection)

    bronxQuery = {'borough': 'Bronx'}
    numberOfRestaurantsInBronx = countDocuments(restaurantsCollection, bronxQuery)

    bronxGradeAQuery = {'borough': 'Bronx', 'grades.grade': 'A'}
    numberOfRestaurantsInBronxWithGradeA = countDocuments(restaurantsCollection, bronxGradeAQuery)

    print('\n{0}\nSTATISTICAL ANALYSIS OF RESTAURANTS\n{0}'.format('='*40))

    print('Total number of restaurants: {}'.format(numberOfRestaurants))
    print('\nTotal number of restaurants in the Bronx: {0}\n% of total restaurants: {1}'.format(numberOfRestaurantsInBronx, (numberOfRestaurantsInBronx * 100 / numberOfRestaurants)))
    print('\nTotal number of restaurants in the Bronx that have gotten an A: {0}\n% of total restaurants in the Bronx: {1}\n% of total restaurants: {2}\n'.format(numberOfRestaurantsInBronxWithGradeA, (numberOfRestaurantsInBronxWithGradeA * 100 / numberOfRestaurantsInBronx), (numberOfRestaurantsInBronxWithGradeA * 100 / numberOfRestaurants)))


test()
