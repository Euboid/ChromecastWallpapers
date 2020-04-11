import requests
import re
import time

while True:
    r = requests.get("https://clients3.google.com/cast/chromecast/home")
    match = re.search(r"(lh4\.googl.+?mv)", r.text).group(1)
    match = match.replace("\\", "")
    match = match.replace("u003d", "=")
    print(match)
    time.sleep(2)
