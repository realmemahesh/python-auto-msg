import time
import schedule
import requests
from credentials import *

def send_message():
    req = requests.post('https://textbelt.com/text',{
        'phone' : mobile_number,
        'message' : 'Testing purpose',
        'key' : 'textbelt'
    })

    print(req.json())

schedule.every(10).seconds.do(send_message)

while True:
  schedule.run_pending()
  time.sleep(1)