import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from a .env file

API_ID = os.getenv('API_ID', '26494161')  
API_HASH = os.getenv('API_HASH', '55da841f877d16a3a806169f3c5153d3')  
BOT_TOKEN = os.getenv('BOT_TOKEN', '7793828619:AAHnY60vTcElNV_Trmd_DE6pKi7y_RKqRO8')  
MONGODB_URL = os.getenv('MONGODB_URL', 'your_mongodb_url')  # MongoDB URL
ADMIN_ID = os.getenv('ADMIN_ID', '7170452349')  # Add admin ID
BOT_IMAGE_URL = os.getenv('BOT_IMAGE_URL', 'https://envs.sh/_Do.jpg')  # Bot's image URL
