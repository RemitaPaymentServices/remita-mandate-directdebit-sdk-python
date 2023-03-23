# Import modules
import requests
import hashlib
from datetime import datetime

# Demo Link
url = "https://remitademo.net/remita/exapp/api/v1/send/api/echannelsvc/echannel/mandate/setup"


# Hash Function
def sha512(input):
    hashed_input = hashlib.sha512(input.encode('utf-8'))
    hex_dig = hashed_input.hexdigest()
    return hex_dig


# Define Variables
merchantId = "27768931"
serviceTypeId = "35126630"
amount = "50000"
apiKey = "Q1dHREVNTzEyMzR8Q1dHREVNTw=="
requestId = str(datetime.now())

# Get the Hash Value
hash = sha512(merchantId + serviceTypeId + requestId + amount + apiKey)

# Define the Payload to Post to the URL
setup_payload = {
    "amount": f"{amount}",
	"endDate": "30/2/2024",
	"hash": f"{hash}",
	"mandateType": "DD",
	"maxNoOfDebits": "3",
	"merchantId": "27768931",
	"payerAccount": "1234890002",
	"payerBankCode": "057",
	"payerEmail": "segunakomolafe7@gmail.com",
	"payerName": "ADEYEMI JAMES",
	"payerPhone": "2345089765647",
	"requestId": f"{requestId}",
	"serviceTypeId": "35126630",
	"startDate": "5/12/2023"
}

# Post the payload to Demo Link
Setup_Post = requests.post(url, json=setup_payload)
print(Setup_Post.text)
