from dotenv import load_dotenv
import requests, os

load_dotenv()

webhook_url = os.environ.get("API_KEY")

def send_discord(message):
    payload = {"content": message}
    response = requests.post(webhook_url, json=payload)
    return response.status_code

send_discord("Hello from Python!")