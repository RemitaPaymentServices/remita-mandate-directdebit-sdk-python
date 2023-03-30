# Import modules
import requests
import hashlib


# Hash Function
def hash512(credentials):
    hashed_input = hashlib.sha512(credentials.encode('utf-8'))
    hex_dig = hashed_input.hexdigest()
    return hex_dig


merchantId = "27768931"
mandateId = "210007800813"
requestId = "payer1"
apiKey = "Q1dHREVNTzEyMzR8Q1dHREVNTw=="
hash = hash512(merchantId + apiKey + requestId)


# URLs
demo_url = "https://remitademo.net/remita/ecomm/mandate/form/"f"{merchantId}""/"f"{hash}""/"f"{mandateId}""/"f"\
{requestId}""/rest.reg"
live_url = "https://login.remita.net/remita/ecomm/mandate/form/"f"{merchantId}""/"f"{hash}""/"f"{mandateId}""/"f"\
{requestId}""/rest.reg"


# Post Function
def get_form(url):
	form_get = requests.get(url)
	return form_get.text


print(get_form(demo_url))
