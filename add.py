import requests
import time

head = {'authority': 'api.faucetpay.io', 'accept': 'application/json, text/plain, */*', 'accept-language': 'en-US,en;q=0.9,id;q=0.8', 'authorization': 'Bearer 3b0860ea9cf70809919281466257689cfef97c1fd24e1d771b7f415e64feab84', 'content-type': 'application/json', 'origin': 'https://faucetpay.io', 'referer': 'https://faucetpay.io/', 'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36'}

file = open("trxAdd.txt", mode='r')

conten = file.read()

wl = conten.split("\n")

def runer(walet, x):
	r = requests.post('https://api.faucetpay.io/wallet/link-address', headers=head, json={"coin": "TRX", "label": "TRONGG " + str(x), "address": str(walet)})
	print(r.text)

x = 0

runer(wl[x], x)