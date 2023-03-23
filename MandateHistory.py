# Import modules
import requests
import hashlib
from datetime import datetime


# Hash Function
def sha512(input):
    hashed_input = hashlib.sha512(input.encode('utf-8'))
    hex_dig = hashed_input.hexdigest()
    return hex_dig


# Demo Link
url = "https://remitademo.net/remita/exapp/api/v1/send/api/echannelsvc/echannel/mandate/payment/history"

merchantId = "27768931"
mandateId = "280007807262"
apiKey = "Q1dHREVNTzEyMzR8Q1dHREVNTw=="
requestId = "1582194580"
hash = sha512(mandateId + merchantId + requestId + apiKey)

History_payload = {
      "merchantId":f"{merchantId}",
      "mandateId":f"{mandateId}",
      "hash":f"{hash}",
      "requestId":f"{requestId}"
}

# Post the payload to Demo Link
Setup_Post = requests.post(url, json=History_payload)
print(Setup_Post.text)
