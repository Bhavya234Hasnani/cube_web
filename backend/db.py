from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
cubexo_db = client["cubexo_db"]

contact_submissions = cubexo_db["submissions"]