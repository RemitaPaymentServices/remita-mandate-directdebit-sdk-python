# Import modules
import requests
import hashlib


# Hash Function
def hash512(credentials):
    hashed_input = hashlib.sha512(credentials.encode('utf-8'))
    hex_dig = hashed_input.hexdigest()
    return hex_dig


# Demo Link
url = "https://remitademo.net/remita/exapp/api/v1/send/api/echannelsvc/echannel/mandate/payment/stop"

merchantId = "27768931"
mandateId = "200007681305"
apiKey = "Q1dHREVNTzEyMzR8Q1dHREVNTw=="
transactionRef = "7681307"
requestId = "1524034885236"
hash = hash512(transactionRef + merchantId + requestId + apiKey)

Cancel_payload = {
      "merchantId": f"{merchantId}",
      "mandateId": f"{mandateId}",
      "transactionRef": f"{transactionRef}",
      "requestId": f"{requestId}",
      "hash": f"{hash}"
}

# Post Function
def cancelpayment(url, Cancel_payload):
	cancel_post = requests.post(url, json=Cancel_payload)
	return cancel_post.text


print(cancelpayment(url, Cancel_payload))
