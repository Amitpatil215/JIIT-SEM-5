import os
import pandas as pd
import numpy as np
import pymongo
from pymongo import MongoClient
from pymongo import mongo_client
from pymongo import collection
print('mongoversion', pymongo.__version__)

client = MongoClient('localjost', 27017)
db = client.test
collection = db.people
