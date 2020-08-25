import random
import requests
import string
import io
from PIL import Image
from io import BytesIO
import os
from os import environ

url_base = "https://cdn2.unrealengine.com/en-14br-teaser-day5-motd-1920x1080-1920x1080-"
jpg_ext = ".jpg"
url_live = 'https://cdn2.unrealengine.com/en-14br-teaser-day1-motd-1920x1080-1920x1080-810893971.jpg'

def download_img(url, file_name):
    r = requests.get(url)
    im = Image.open(BytesIO(r.content))
    im.save(ImageID + '.jpg')

number_start = 848500000

while 1:
    try:
        number_current = number_start + 1
        url = url_base + str(number_current) + jpg_ext
        url_status = requests.get(url)
        status = url_status.status_code
        print(url)
        print(status)
        if status == 200:
            try:
                print('Imagen detectada.')
                print(number_current)
                ImageID = str(number_current)
                file = (ImageID + '.jpg')
                download_img(url, file)
                print('Se ha guardado correctamente.')
            except:
                print('Error al descargar.')
        number_start = number_current

    except:
        print('Err.')





