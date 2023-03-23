# Import modules
import requests
import hashlib


# Hash Function
def sha512(input):
    hashed_input = hashlib.sha512(input.encode('utf-8'))
    hex_dig = hashed_input.hexdigest()
    return hex_dig


# Demo Link
url = "https://remitademo.net/remita/exapp/api/v1/send/api/echannelsvc/echannel/mandate/payment/status"

mandateId = "140007735469"
merchantId = "27768931"
requestId = "1551782788673"
apiKey = "Q1dHREVNTzEyMzR8Q1dHREVNTw=="
hash = sha512(mandateId + merchantId + requestId + apiKey)

Status_payload = {
      "merchantId": f"{merchantId}",
      "mandateId": f"{mandateId}",
      "hash": f"{hash}",
      "requestId": f"{requestId}"
}


# Post the payload to Demo Link
Setup_Post = requests.post(url, json=Status_payload)
print(Setup_Post.text)
