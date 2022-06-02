from urllib.request import urlopen, Request
# 
from time import sleep
# import app

httprequest = Request("https://icanhazip.com", headers={"Accept": "application/json"})
with urlopen(httprequest) as response:
    print(response.status)
    print(response.read().decode())

sleep(30)
# app()
