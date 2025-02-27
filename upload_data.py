from pymongo.mongo_client import MongoClient
import pandas as pd
import json

url = "mongodb+srv://personalhp1805:MifxAWaCbqfphyHv@cluster0.qu9in.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(url)

DATABASE_NAME="pwskills"
COLLECTION_NAME="waferfault"

df = pd.read_csv("D:\Sensor fault detection\notebooks\wafer_23012020_041211.csv")

df = df.drop("Unnamed: 0", axis=1)

json_record = list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)