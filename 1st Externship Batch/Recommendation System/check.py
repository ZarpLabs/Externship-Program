import requests
import json 
import time


start = time.time()
url = 'https://recommendation--api.herokuapp.com/'
data = 'ledger'
data = json.dumps(data)
rqt = requests.post(url, data)
end = time.time()
print(rqt.json())
print('Runtime {:.2f} seconds'.format(end-start))