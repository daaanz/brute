import random
import requests
import string
import tweepy
import io
from PIL import Image
from io import BytesIO

auth = tweepy.OAuthHandler("wZdsf58Ka2jciAifsd5NDg2y1", "FwbZcX6g9vGbpwLyNejLIHdY9KybOhUdEBHVTvXn6YQpa1MpRY")
auth.set_access_token("1285954782545563649-gM0P4hinHv47aYX9EATIgidTOzxS89", "9vBzMVJOh21YbylaR01cwQZs3T1zhRCvKScFHFMsbEoci")
api = tweepy.API(auth)

url_base = "https://cdn2.unrealengine.com/en-14br-teaser-day4-motd-1920x1080-1920x1080-"
jpg_ext = ".jpg"
url_live = 'https://cdn2.unrealengine.com/en-14br-teaser-day1-motd-1920x1080-1920x1080-810893971.jpg'

def download_img(url, file_name):
    r = requests.get(url)
    im = Image.open(BytesIO(r.content))
    im.save(number_current + '.jpg')

number_start = 820000000

while 1:
    try:
        number_current = number_start + 1
        url = url_base + str(number_current) + jpg_ext
        url_status = requests.get(url)
        status = url_status.status_code
        print(url)
        print(status)
        number_start = number_current
        if status == '200':
            print('Imagen detectada.')
            file = (number_current + '.jpg')
            download_img(url, file)
            print('Se ha guardado correctamente.')
            api.update_with_media(number_current + '.jpg', 'text')
            print('Se ha publicado en Twitter')
    except:
        print('Err.')





