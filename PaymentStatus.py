# Import modules
import requests
import hashlib


# Hash Function
def hash512(credentials):
    hashed_input = hashlib.sha512(credentials.encode('utf-8'))
    hex_dig = hashed_input.hexdigest()
    return hex_dig


# URLs
demo_url = "https://remitademo.net/remita/exapp/api/v1/send/api/echannelsvc/echannel/mandate/payment/status"
live_url = "https://login.remita.net/remita/exapp/api/v1/send/api/echannelsvc/echannel/mandate/payment/status"


mandateId = "140007735469"
merchantId = "27768931"
requestId = "1551782788673"
apiKey = "Q1dHREVNTzEyMzR8Q1dHREVNTw=="
hash = hash512(mandateId + merchantId + requestId + apiKey)

Status_payload = {
      "merchantId": f"{merchantId}",
      "mandateId": f"{mandateId}",
      "hash": f"{hash}",
      "requestId": f"{requestId}"
}


# Post Function
def paymentstatus(url, Status_payload):
	paymentstatus_post = requests.post(url, json=Status_payload)
	return paymentstatus_post.text


print(paymentstatus(demo_url, Status_payload))
