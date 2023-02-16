from urllib.request import urlopen
import sys
from time import sleep

sec = int(sys.argv[1])

print("python urllib started")

while True:
  sleep(sec)
  with urlopen('https://custom-service') as response:
    print(response.read())
