from time import sleep
from requests import get
import random
import requests
import os

ip = get('https://checkip.amazonaws.com').text.strip()
ports = [os.environ['APP_PORT_1'], os.environ['APP_PORT_2'], os.environ['APP_PORT_3']]

while True:
    sleep_time = random.randint(10, 40)
    print(f"Sleeping for {sleep_time}")
    sleep(sleep_time)

    port = random.choice(ports)
    requests.get(f"http://{ip}:{port}/endpoint")


