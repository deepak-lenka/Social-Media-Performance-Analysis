import os
import random
from datetime import datetime, timedelta
from dotenv import load_dotenv
from astrapy.db import AstraDB
import uuid

# Load environment variables
load_dotenv()

# Astra DB Configuration
ASTRA_DB_APPLICATION_TOKEN = os.getenv('ASTRA_DB_APPLICATION_TOKEN')

# Initialize the client
db = AstraDB(
    token=ASTRA_DB_APPLICATION_TOKEN,
    api_endpoint="https://a989e7a0-77e1-455f-a09f-e317ee50519f-us-east1.apps.astra.datastax.com"
)

# Create collection if it doesn't exist
collection_name = 'posts'
try:
    collection = db.collection(collection_name)
    # Test if collection exists by trying to access it
    collection.find_one({})
except:
    # Collection doesn't exist, create it
    db.create_collection(collection_name)
    collection = db.collection(collection_name)

# Clear existing data
collection.delete_many({})

# Generate mock data
post_types = ['carousel', 'reel', 'static']
num_posts = 100

for _ in range(num_posts):
    post_data = {
        '_id': str(uuid.uuid4()),  # Required by Astra DB
        'post_id': str(uuid.uuid4()),
        'post_type': random.choice(post_types),
        'likes': random.randint(50, 1000),
        'shares': random.randint(10, 200),
        'comments': random.randint(5, 100),
        'created_at': (datetime.now() - timedelta(days=random.randint(0, 30))).isoformat()
    }
    
    # Insert data into Astra DB
    collection.insert_one(post_data)

print(f"Generated and stored {num_posts} mock posts in Astra DB") 