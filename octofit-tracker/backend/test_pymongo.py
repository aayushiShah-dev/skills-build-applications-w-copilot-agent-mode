from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('localhost', 27017)
db = client['octofit_db']

# Insert test data
test_data = {"name": "Test User", "email": "testuser@example.com"}
result = db.users.insert_one(test_data)
print(f"Inserted document ID: {result.inserted_id}")

# Retrieve test data
retrieved_data = db.users.find_one({"email": "testuser@example.com"})
print(f"Retrieved document: {retrieved_data}")

# Clean up
db.users.delete_one({"email": "testuser@example.com"})
print("Test document deleted.")
