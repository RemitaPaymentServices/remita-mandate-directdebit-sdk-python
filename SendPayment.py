# Import modules
import requests
import hashlib
from datetime import datetime

# Demo Link
url = "https://remitademo.net/remita/exapp/api/v1/send/api/echannelsvc/echannel/mandate/payment/send"


# Hash Function
def sha512(input):
    hashed_input = hashlib.sha512(input.encode('utf-8'))
    hex_dig = hashed_input.hexdigest()
    return hex_dig


merchantId = "27768931"
serviceTypeId = "35126630"
mandateId = "280007806861"
requestId = datetime.now().strftime("%H%M%S%f")
amount = "500"
apiKey = "Q1dHREVNTzEyMzR8Q1dHREVNTw=="

hash = sha512(merchantId + serviceTypeId + requestId + amount + apiKey)

Pay_payload = {
      "merchantId": f"{merchantId}",
      "serviceTypeId": f"{serviceTypeId}",
      "hash": f"{hash}",
      "requestId": f"{requestId}",
      "totalAmount": f"{amount}",
      "mandateId": f"{mandateId}",
      "fundingAccount": "3072119052",
      "fundingBankCode": "057"
}

# Post the payload to Demo Link
Setup_Post = requests.post(url, json=Pay_payload)
print(Setup_Post.text)
