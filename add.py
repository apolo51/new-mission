import requests
import time

head = {'authority': 'api.faucetpay.io', 'accept': 'application/json, text/plain, */*', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9,id;q=0.8', 'authorization': 'Bearer 3b0860ea9cf70809919281466257689cfef97c1fd24e1d771b7f415e64feab84', 'content-type': 'application/json', 'origin': 'https://faucetpay.io', 'referer': 'https://faucetpay.io/', 'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36'}

file = open("trxAdd.txt", mode='r')

conten = file.read()

list = conten.split("\n")
#print(list)
x = 0
while True :
	if x <= 7190 :
		walet = str(list[x])

		x+=1

		r = requests.post('https://api.faucetpay.io/wallet/link-address', headers=head, json={"coin": "TRX", "label": "TRONGG " + str(x), "address": str(walet)})
		time.sleep(10)
	else :
		print('SUDAH HABIS')