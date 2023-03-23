# Import modules
import requests
import hashlib


# Hash Function
def sha512(input):
    hashed_input = hashlib.sha512(input.encode('utf-8'))
    hex_dig = hashed_input.hexdigest()
    return hex_dig


# Demo Link
url = "https://remitademo.net/remita/exapp/api/v1/send/api/echannelsvc/echannel/mandate/stop"

mandateId = "150007761106"
merchantId = "27768931"
requestId = "1564489623447"
apiKey = "Q1dHREVNTzEyMzR8Q1dHREVNTw=="
hash = sha512(mandateId + merchantId + requestId + apiKey)

Stop_payload = {
      "merchantId": f"{merchantId}",
      "hash": f"{hash}",
      "mandateId": f"{mandateId}",
      "requestId": f"{requestId}"
}

# Post the payload to Demo Link
Setup_Post = requests.post(url, json=Stop_payload)
print(Setup_Post.text)
