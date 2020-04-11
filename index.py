import requests
import re
import time
from PIL import Image
from io import BytesIO

links = list()

# Get Number of Chromecast Images User Would Like
nos = int(input("How many chromecast images would you like to download? "))
server = int(input("Pick Server (3 - 6): "))
cur = 0

while True:
    if cur == nos:
        break
    else:
        r = requests.get("https://clients3.google.com/cast/chromecast/home")
        match = re.search(r"(lh{}\.googl.+?mv)".format(str(server)), r.text).group(1)
        match = match.replace("\\", "")
        match = match.replace("u003d", "=")
        match = 'https://' + match
        links.append(match)
        print("Extracting link: " + str(cur + 1))
        time.sleep(1)
        cur += 1


ident = 0
unique_list = list()
for link in links:
    ident += 1
    # Check if image is unique
    if link not in unique_list:
        print("Saving Image", str(ident))
        # Save file
        try:
            response = requests.get(link)
            img = Image.open(BytesIO(response.content))
            img.save('chromecast_i' + str(ident) + '.png')
        except Exception:
            print("Bad IMAGE!")
