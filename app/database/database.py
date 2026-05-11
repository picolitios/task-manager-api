from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

class MongoDBManager:
    client: AsyncIOMotorClient = None
    db = None

    def connect(self):
        self.client = AsyncIOMotorClient(settings.MONGODB_URL)
        self.db = self.client[settings.DATABASE_NAME]
        print("Connected to MongoDB via Motor.")

    def close(self):
        if self.client:
            self.client.close()
            print("Closed MongoDB connection.")

db_manager = MongoDBManager()

def get_db():
    return db_manager.db
