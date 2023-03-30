# Import modules
import requests
import hashlib


# Hash Function
def hash512(credentials):
    hashed_input = hashlib.sha512(credentials.encode('utf-8'))
    hex_dig = hashed_input.hexdigest()
    return hex_dig


# URLs
demo_url = "https://remitademo.net/remita/exapp/api/v1/send/api/echannelsvc/echannel/mandate/stop"
live_url = "https://login.remita.net/remita/exapp/api/v1/send/api/echannelsvc/echannel/mandate/stop"


mandateId = "150007761106"
merchantId = "27768931"
requestId = "1564489623447"
apiKey = "Q1dHREVNTzEyMzR8Q1dHREVNTw=="
hash = hash512(mandateId + merchantId + requestId + apiKey)

Stop_payload = {
      "merchantId": f"{merchantId}",
      "hash": f"{hash}",
      "mandateId": f"{mandateId}",
      "requestId": f"{requestId}"
}


# Post Function
def stopmandate(url,  Stop_payload):
	stopmandate_post = requests.post(url, json=Stop_payload)
	return stopmandate_post.text


print(stopmandate(demo_url, Stop_payload))
