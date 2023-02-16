from time import sleep
import sys
import requests

sec = int(sys.argv[1])

print("Python started")

while True:
  sleep(sec)
  print("requesting https://custom-service")
  res = requests.get('https://custom-service', verify='/usr/certs/bundle.crt')
  print(res)
