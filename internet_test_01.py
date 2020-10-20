from PIL import Image
import shutil
import requests
import os
import glob
from pprint import pprint

test_image_url = requests.get("https://cdn.pixabay.com/photo/2020/02/06/09/39/summer-4823612_960_720.jpg")

file_name = test_image_url.split("/")[-1]

request = requests.get(test_image_url, stream = True)

if request.status_code == 200:
    request.raw.decode_content = True

    with open(file_name, "wb") as f:
        shutil.copyfileobj(request.raw, f)
    print(file_name, " was successfully downloaded.")
    file_name.show()
else:
    print("The requested image could not be found.")
