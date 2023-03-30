# Import modules
import requests
import hashlib
from datetime import datetime

# URLs
demo_url = "https://remitademo.net/remita/exapp/api/v1/send/api/echannelsvc/echannel/mandate/setup"
live_url = "https://login.remita.net/remita/exapp/api/v1/send/api/echannelsvc/echannel/mandate/setup"


# Hash Function
def hash512(credentials):
    hashed_input = hashlib.sha512(credentials.encode('utf-8'))
    hex_dig = hashed_input.hexdigest()
    return hex_dig


# Credentials
requestId = str(datetime.now())
merchantId = "27768931"
serviceTypeId = "35126630"
apiKey = "Q1dHREVNTzEyMzR8Q1dHREVNTw=="


# Define Variables
mandatetype = "DD"
amount = "50000"
maxNoOfDebits = "3"
startDate = "5/12/2023"
enddate = "30/2/2024"
payerAccount = "1234890002"
payerEmail = "segunakomolafe7@gmail.com"
payerName = "ADEYEMI JAMES"
payerPhone = "2345089765647"
payerBankCode = "057"

# Get the Hash Value
hash = hash512(merchantId + serviceTypeId + requestId + amount + apiKey)

# The Payload to Post to the URL
setup_payload = {
    "amount": f"{amount}",
    "startDate": f"{startDate}",
	"endDate": f"{enddate}",
    "hash": f"{hash}",
	"mandateType": f"{mandatetype}",
	"maxNoOfDebits": f"{maxNoOfDebits}",
	"payerAccount": f"{payerAccount}",
	"payerBankCode": f"{payerBankCode}",
	"payerEmail": f"{payerEmail}",
	"payerName": f"{payerName}",
	"payerPhone": f"{payerPhone}",
    "merchantId": f"{merchantId}",
	"requestId": f"{requestId}",
	"serviceTypeId": f"{serviceTypeId}",
}


# Post Function
def mandatesetup(url, setup_payload):
	Setup_Post = requests.post(url, json=setup_payload)
	return Setup_Post.text


print(mandatesetup(demo_url, setup_payload))
