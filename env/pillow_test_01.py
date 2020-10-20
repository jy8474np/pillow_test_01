from PIL import Image
import requests
import os

bridge = Image.open("/Users/mtlynchjr/Desktop/Final Semester/pillow_test_01/env/golden_gate.jpg") # Image opened from directory folder
batman = Image.open("https://upload.wikimedia.org/wikipedia/en/8/87/Batman_DC_Comics.png") # Image obtained from website

# "/Users/mtlynchjr/Desktop/Final Semester/pillow_test_01/env/golden_gate.jpg"

bridge.save("/Users/mtlynchjr/Desktop/Final Semester/pillow_test_01/env/bridge_displayed_image.jpg") # Saves image opened from directory and saves it as a "displayed image"
bridge.show() # Displays machine image to usuer (via their machine's default image viewer)

batman.save("/Users/mtlynchjr/Desktop/Final Semester/pillow_test_01/env/batman_displayed_image.jpg") # Saves image obtained from Internet and saves it as a "displayed image"
bridge.show() # Displays Internet image to usuer (via their machine's default image viewer)
