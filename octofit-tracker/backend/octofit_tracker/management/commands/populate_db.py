from pymongo import MongoClient

def populate():
    client = MongoClient("mongodb://localhost:27017")
    db = client["octofit_db"]

    # Required minimal test data
    db.users.insert_one({"name": "Test User"})
    db.activities.insert_one({"activity": "Test Activity"})

    print("Database populated.")

if __name__ == "__main__":
    populate()