import os
import openai
from dotenv import load_dotenv
from django.core.files import File
import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


def GPT_function(name):
    try:
        response = openai.Image.create(
            prompt=f"{name}", n=1, size="1024x1024"
        )
        image_url = response['data'][0]['url']
        return image_url
    except Exception as e:
        print(e)
        return 'http://unavailable'


def creating_picture(obj):
    if obj.picture_url and not obj.picture:
        result = urllib.request.urlretrieve(obj.picture_url)
        obj.picture.save(
            os.path.basename(obj.picture_url),
            File(open(result[0], 'rb'))
        )
        obj.save()
