
# importing module
from pymongo import MongoClient

# creation of MongoClient
client = MongoClient()

# Connect with the portnumber and host
client = MongoClient("mongodb://localhost:27017/")

# Access database
mydatabase = client["sname_of_the_database"]

# Access collection of the database
mycollection = mydatabase["myTable"]

# dictionary to be added in the database
rec = {
    'title': 'MongoDB and Python',
    'description': 'MongoDB is no SQL database',
    'tags': ['mongodb', 'database', 'NoSQL'],
    'viewers': 104
}

# inserting the data in the database
# rec = mydatabase.myTable.insert_many(rec)

# To find() all the entries inside collection name 'myTable
cursor = mycollection.find()
for record in cursor:
    print(record)
