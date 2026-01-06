from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
ABUSEIPDB_API_KEY = os.getenv("ABUSEIPDB_API_KEY")
ABUSEIPDB_BASE_URL = "https://api.abuseipdb.com/api/v2/check"