from PIL import Image
import shutil
import requests
import os
import glob
from pprint import pprint

bridge = Image.open("/Users/mtlynchjr/Desktop/Final Semester/pillow_test_01/env/golden_gate.jpg") # Image opened from directory folder

# batman_url = requests.get("https://upload.wikimedia.org/wikipedia/en/8/87/Batman_DC_Comics.png") # Image obtained from website
# batman_info = batman_url.json() # Assigns image response to variable "batman_info"
# batman_image = batman_info["Batman_DC_Comics.png"]

# "/Users/mtlynchjr/Desktop/Final Semester/pillow_test_01/env/golden_gate.jpg"

bridge.save("/Users/mtlynchjr/Desktop/Final Semester/pillow_test_01/env/bridge_displayed_image.jpg") # Saves image opened from directory and saves it as a "displayed image"
bridge.show() # Displays machine image to usuer (via their machine's default image viewer)

# batman_url.save("/Users/mtlynchjr/Desktop/Final Semester/pillow_test_01/env/batman_displayed_image.jpg") # Saves image obtained from Internet and saves it as a "displayed image"
# batman_url.show() # Displays Internet image to usuer (via their machine's default image viewer)
