from pymongo.mongo_client import MongoClient

# Replace with the actual password, URL-encoded if needed
uri = "mongodb+srv://abhiramgajula9:ABHIRAM6@cluster0.cz9vlde.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri)

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print("Failed to connect:", e)
