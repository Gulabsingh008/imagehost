import os
from motor.motor_asyncio import AsyncIOMotorClient  


MONGODB_URL = os.getenv('MONGODB_URL', 'mongodb+srv://lokendrasaini9galaxy:f0TVDwu5pVrHn5i6@cluster0.zseht.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')

class MongoDB:
    def __init__(self, url):
        self.client = AsyncIOMotorClient(url)
        self.db = self.client['imagehost_db']  
        self.uploads_collection = self.db['uploads']  
        self.users_collection = self.db['users']      

    async def insert_upload(self, file_url):
        """Insert uploaded file URL into the database."""
        try:
            await self.uploads_collection.insert_one({"file_url": file_url})
        except Exception as e:
            print(f"Error inserting upload: {e}")

    async def get_all_uploads(self):
        """Get all uploaded file URLs from the database."""
        try:
            return await self.uploads_collection.find({}, {"_id": 0, "file_url": 1}).to_list(length=None)
        except Exception as e:
            print(f"Error fetching uploads: {e}")
            return []

    async def count_uploads(self):
        """Get the total count of uploads."""
        try:
            return await self.uploads_collection.count_documents({})
        except Exception as e:
            print(f"Error counting uploads: {e}")
            return 0

    async def insert_user(self, user_id):
        """Insert a new user into the users collection."""
        try:
            await self.users_collection.insert_one({"user_id": user_id})
        except Exception as e:
            print(f"Error inserting user: {e}")

    async def add_or_update_user(self, user_data):
        """Add a new user or update existing user data."""
        try:
            await self.users_collection.update_one(
                {"user_id": user_data["user_id"]},
                {"$set": user_data},
                upsert=True
            )
        except Exception as e:
            print(f"Error updating user data: {e}")

    async def count_users(self):
        """Get the total count of users."""
        try:
            return await self.users_collection.count_documents({})
        except Exception as e:
            print(f"Error counting users: {e}")
            return 0

    async def get_total_users(self):
        """Get the total number of users."""
        try:
            return await self.count_users()  
        except Exception as e:
            print(f"Error fetching total users: {e}")
            return 0

    async def get_all_user_ids(self):
        """Get all user IDs from the users collection."""
        try:
            cursor = self.users_collection.find({}, {"_id": 0, "user_id": 1})  
            user_ids = await cursor.to_list(length=None)  
            return [user['user_id'] for user in user_ids]  
        except Exception as e:
            print(f"Error fetching user IDs: {e}")
            return []

async def connect_to_mongodb():
    """Connect to MongoDB and return the MongoDB instance."""
    return MongoDB(MONGODB_URL)


mongo_db = MongoDB(MONGODB_URL)

#My mongo_db.py and wait I am giving my init then analyse the codes and then give updated codes ok?
