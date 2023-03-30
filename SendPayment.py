# Import modules
import requests
import hashlib
from datetime import datetime

# URLs
demo_url = "https://remitademo.net/remita/exapp/api/v1/send/api/echannelsvc/echannel/mandate/payment/send"
live_url = "https://login.remita.net/remita/exapp/api/v1/send/api/echannelsvc/echannel/mandate/payment/send"


# Hash Function
def hash512(credentials):
    hashed_input = hashlib.sha512(credentials.encode('utf-8'))
    hex_dig = hashed_input.hexdigest()
    return hex_dig


merchantId = "27768931"
serviceTypeId = "35126630"
mandateId = "280007806861"
requestId = datetime.now().strftime("%H%M%S%f")
amount = "500"
apiKey = "Q1dHREVNTzEyMzR8Q1dHREVNTw=="
fundingAccount = "3072119052"
fundingBankCode = "057"
hash = hash512(merchantId + serviceTypeId + requestId + amount + apiKey)

Pay_payload = {
      "merchantId": f"{merchantId}",
      "serviceTypeId": f"{serviceTypeId}",
      "hash": f"{hash}",
      "requestId": f"{requestId}",
      "totalAmount": f"{amount}",
      "mandateId": f"{mandateId}",
      "fundingAccount": f"{fundingAccount}",
      "fundingBankCode": f"{fundingBankCode}"
}


# Post Function
def sendpayment(url, Pay_payload):
	sendpayment_post = requests.post(url, json=Pay_payload)
	return sendpayment_post.text


print(sendpayment(demo_url, Pay_payload))
