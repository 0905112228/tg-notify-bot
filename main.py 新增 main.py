import os
import requests
from flask import Flask, request

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHANNEL_ID,
        "text": text
    }
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print("Error sending message:", e)

@app.route("/", methods=["GET"])
def home():
    return "土地公推播系統啟動成功"

@app.route("/notify", methods=["POST"])
def notify():
    data = request.json
    message = data.get("message", "沒有內容")
    send_message(message)
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
