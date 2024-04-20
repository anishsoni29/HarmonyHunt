from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the database credentials from environment variables
DB_USER = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")