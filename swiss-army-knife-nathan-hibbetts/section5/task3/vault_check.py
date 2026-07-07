from dotenv import load_dotenv
import os

load_dotenv()  # looks for .env in the current working directory by default

api_key = os.getenv("SUPER_SECRET_KEY")

masked = "*" * (len(api_key) - 3) + api_key[-3:]
print(masked)