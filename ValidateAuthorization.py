# Import modules
import requests
import hashlib
from datetime import datetime

# Demo Link
demo_url = "https://remitademo.net/remita/exapp/api/v1/send/api/echannelsvc/echannel/mandate/validateAuthorization"
live_url = "https://login.remita.net/remita/exapp/api/v1/send/api/echannelsvc/echannel/mandate/validateAuthorization"


# Hash Function
def hash512(credentials):
    hashed_input = hashlib.sha512(credentials.encode('utf-8'))
    hex_dig = hashed_input.hexdigest()
    return hex_dig


merchantId = "27768931"
apiKey = "Q1dHREVNTzEyMzR8Q1dHREVNTw=="
apiToken = "SGlQekNzMEdMbjhlRUZsUzJCWk5saDB6SU14Zk15djR4WmkxaUpDTll6bGIxRCs4UkVvaGhnPT0="
requestId = datetime.now().strftime("%H%M%S%f")
requestTS = datetime.now().strftime("%y-%m-%dT%H:%M:%S:%f")
apiHash = hash512(apiKey + requestId + apiToken)

otp = "1234"
card = "0441234567890"
remitaTransRef = "1627049255216"


otp_payload = {
     "remitaTransRef": f"{remitaTransRef}",
     "authParams": [
      {
       "param1": "OTP",
       "value": f"{otp}"
      },
      {
       "param2": "CARD",
       "value": f"{card}"
      }
     ]
}

headers = {
    "MERCHANT_ID": f"{merchantId}",
    "API_KEY": f"{apiKey}",
    "REQUEST_ID": f"{requestId}",
    "REQUEST_TS": f"{requestTS}",
    "API_DETAILS_HASH": f"{apiHash}"
          }


# Post Function
def validateotp(url, headers, otp_payload):
	validateotp_post = requests.post(url, headers=headers, json=otp_payload)
	return validateotp_post.text


print(validateotp(demo_url, headers, otp_payload))
