from PIL import Image
import requests
import os
from pprint import pprint

bridge = Image.open("/Users/mtlynchjr/Desktop/Final Semester/pillow_test_01/env/golden_gate.jpg") # Existing image opened from directory folder

bridge.show() # Displays directory image to user via their machine's default image viewer

bridge.save("/Users/mtlynchjr/Desktop/Final Semester/pillow_test_01/env/bridge_displayed_image.jpg") # Saves image opened from directory folder to project folder as a "displayed image"
