# Import modules
import requests
import hashlib
from datetime import datetime


# Hash Function
def hash512(credentials):
    hashed_input = hashlib.sha512(credentials.encode('utf-8'))
    hex_dig = hashed_input.hexdigest()
    return hex_dig


# Demo Link
url = "https://remitademo.net/remita/exapp/api/v1/send/api/echannelsvc/echannel/mandate/payment/history"

merchantId = "27768931"
mandateId = "280007807262"
apiKey = "Q1dHREVNTzEyMzR8Q1dHREVNTw=="
requestId = "1582194580"
hash = hash512(mandateId + merchantId + requestId + apiKey)

History_payload = {
      "merchantId": f"{merchantId}",
      "mandateId": f"{mandateId}",
      "hash": f"{hash}",
      "requestId": f"{requestId}"
}

# Post Function
def checkhistory(url, History_payload):
	history_post = requests.post(url, json=History_payload)
	return history_post.text


print(checkhistory(url, History_payload))
