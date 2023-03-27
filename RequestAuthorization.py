# Import modules
import requests
import hashlib
from datetime import datetime

# Demo Link
url = "https://remitademo.net/remita/exapp/api/v1/send/api/echannelsvc/echannel/mandate/requestAuthorization"


# Hash Function
def hash512(credentials):
    hashed_input = hashlib.sha512(credentials.encode('utf-8'))
    hex_dig = hashed_input.hexdigest()
    return hex_dig


mandateId = "220008231534"
requestID = "1626109625683"
merchantId = "27768931"
apiKey = "Q1dHREVNTzEyMzR8Q1dHREVNTw=="
apiToken = "SGlQekNzMEdMbjhlRUZsUzJCWk5saDB6SU14Zk15djR4WmkxaUpDTll6bGIxRCs4UkVvaGhnPT0="
requestId = datetime.now().strftime("%H%M%S%f")
requestTS = datetime.now().strftime("%y-%m-%dT%H:%M:%S:%f")
apiHash = hash512(apiKey + requestId + apiToken)

otp_payload = {
   "mandateId": f"{mandateId}",
   "requestId": f"{requestID}"
}

headers = {
    "MERCHANT_ID": f"{merchantId}",
    "API_KEY": f"{apiKey}",
    "REQUEST_ID": f"{requestId}",
    "REQUEST_TS": f"{requestTS}",
    "API_DETAILS_HASH": f"{apiHash}"
          }


# Post Function
def requestotp(url, headers, otp_payload):
	otp_post = requests.post(url, headers=headers, json=otp_payload)
	return otp_post.text


print(requestotp(url, headers, otp_payload))
