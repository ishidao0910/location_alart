# utils/send_line_message.py
import requests

BASE_URL = "https://api.line.me/v2/bot/message/push"

def send_line_message(token, user_id, message_text):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    data = {
        "to": user_id,
        "messages": [
            {
                "type": "text",
                "text": message_text
            }
        ]
    }
    response = requests.post(BASE_URL, headers=headers, json=data)
    return response
