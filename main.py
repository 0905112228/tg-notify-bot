from flask import Flask, request
import os
import requests

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

# 新增這兩個 route，解決 404 問題
@app.route('/', methods=['GET'])
def index():
    return '土地公上線囉！'

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    if data and 'message' in data and 'text' in data['message']:
        text = data['message']['text']
        send_message(f"土地公收到訊息：{text}")
    return 'OK'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
