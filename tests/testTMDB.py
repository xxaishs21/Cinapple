from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv("TMDB_BEARER_TOKEN")
print(token)