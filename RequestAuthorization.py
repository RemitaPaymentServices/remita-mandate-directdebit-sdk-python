# Import modules
import requests
import hashlib
from datetime import datetime

# Demo Link
url = "https://remitademo.net/remita/exapp/api/v1/send/api/echannelsvc/echannel/mandate/requestAuthorization"


# Hash Function
def sha512(input):
    hashed_input = hashlib.sha512(input.encode('utf-8'))
    hex_dig = hashed_input.hexdigest()
    return hex_dig


otp_payload = {
   "mandateId": "220008231534",
   "requestId": "1626109625683"
}

merchantId = "27768931"
apiKey = "Q1dHREVNTzEyMzR8Q1dHREVNTw=="
apiToken = "SGlQekNzMEdMbjhlRUZsUzJCWk5saDB6SU14Zk15djR4WmkxaUpDTll6bGIxRCs4UkVvaGhnPT0="
requestId = datetime.now().strftime("%H%M%S%f")
requestTS = datetime.now().strftime("%y-%m-%dT%H:%M:%S:%f")
apiHash = sha512(apiKey + requestId + apiToken)


headers = {
    "MERCHANT_ID": "27768931",
    "API_KEY": "Q1dHREVNTzEyMzR8Q1dHREVNTw==",
    "REQUEST_ID": f"{requestId}",
    "REQUEST_TS": f"{requestTS}",
    "API_DETAILS_HASH": f"{apiHash}"
          }


# Post the payload to Demo Link
otp_Post = requests.post(url, headers=headers, json=otp_payload)
print(otp_Post.text)
