#!/usr/bin/python
# -*- coding: utf-8 -*-

import  subprocess
import requests
import json

url_login = 'https://mcs.mail.ru/api/v1/auth/signin'
url_main = 'https://mcs.mail.ru/api/v1/projects/mcsXXXXXXXX/billing'

payload = {
    'email': 'ant@XXXX.XXX',
    'password': 'XXXXXXX',
}
 
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Host': 'mcs.mail.ru',
    'Content-Type': 'application/json;charset=utf-8',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0',
    'Referer': 'https://mcs.mail.ru/app/auth/',
    'x-email': 'ant@XXXX.XX',
    'X-Requested-With': 'XMLHttpRequest',
    'TE': 'Trailers',
    'Host': 'mcs.mail.ru',
    'Origin': 'https://mcs.mail.ru'
}
 

s = requests.Session() 
r = s.post(url_login, json=payload, headers=headers)
 

cookies = r.cookies.get_dict()
cookies['_identity_hosting'] = 'df0fc8bda049e5a8153084d6bf3e040af258179c5e68b49276f445b7acbc9537a%3A2%3A%7Bi%3A0%3Bs%3A17%3A%22_identity_hosting%22%3Bi%3A1%3Bs%3A58%3A%22%5B%22ci91199%22%2C%22e8d68688-ef73-4b01-bf6f-b2a245770b56%22%2C2592000%5D%22%3B%7D'
 
r2 = s.get(url_main, headers=headers)

res = json.loads(r2.text)
 
if r2.status_code == 200:
    print(res['balance'])
