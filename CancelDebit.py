# Import modules
import requests
import hashlib


# Hash Function
def sha512(input):
    hashed_input = hashlib.sha512(input.encode('utf-8'))
    hex_dig = hashed_input.hexdigest()
    return hex_dig


# Demo Link
url = "https://remitademo.net/remita/exapp/api/v1/send/api/echannelsvc/echannel/mandate/payment/stop"

merchantId = "27768931"
mandateId = "200007681305"
apiKey = "Q1dHREVNTzEyMzR8Q1dHREVNTw=="
transactionRef = "7681307"
requestId = "1524034885236"
hash = sha512(transactionRef + merchantId + requestId + apiKey)

Cancel_payload = {
      "merchantId": f"{merchantId}",
      "mandateId": f"{mandateId}",
      "transactionRef": f"{transactionRef}",
      "requestId": f"{requestId}",
      "hash": f"{hash}"
}

# Post the payload to Demo Link
Setup_Post = requests.post(url, json=Cancel_payload)
print(Setup_Post.text)
