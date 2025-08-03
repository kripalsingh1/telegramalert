from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "7962131421:AAFgZruC54XSLbTI0r7-TvNUF72hc151P0E"
CHAT_ID = "-1001399382341"  # 👈 Updated with your channel ID

@app.route('/', methods=['POST'])
def send_telegram():
    data = request.json
    message = data.get("message", "No message received")

    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    requests.post(telegram_url, data=payload)

    return 'OK', 200
