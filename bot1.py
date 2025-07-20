import requests

TOKEN = "Bot_Token" 
chat_id = "Chat_ID"

message = "Your Code has finished running !"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"

print(requests.get(url).json()) # this sends the message
