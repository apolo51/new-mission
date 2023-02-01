import requests
import time
import json

authb = input('AUTH KEY : ')

head = {'authority': 'api.faucetpay.io', 'accept': 'application/json, text/plain, */*', 'accept-language': 'en-US,en;q=0.9,id;q=0.8', 'authorization': str(authb), 'content-type': 'application/json', 'origin': 'https://faucetpay.io', 'referer': 'https://faucetpay.io/', 'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36'}

file = open("trxAdd.txt", mode='r')

conten = file.read()

wl = conten.split("\n")

def runer(walet, x): 
	r = requests.post('https://api.faucetpay.io/wallet/link-address', headers=head, json={"coin": "TRX", "label": "TRONGG " + str(x), "address": str(walet)})
	return r.text

x = 499

while x < 8000:
	coba = runer(wl[x], x)
	print(coba)
	if coba == '{"success":false,"message":"You have reached the maximum number of linked addresses."}':
		x = 8001
	if coba == '{"success":true,"message":"Great news! The address has been linked to your account."}' or '{"success":false,"message":"This address is already linked to your account."}':
		x+=1
		time.sleep(1)
	else:
		print('Wait 5 Sec')
		time.sleep(5)