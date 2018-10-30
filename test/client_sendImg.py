import requests, json
import cv2
import numpy as np


#init
url='http://127.0.0.1:5000/human'

img = cv2.imread("knowns_hg.jpg");
ret, jpg = cv2.imencode('.jpg', img)
jpg_to_bytes = jpg.tobytes()

response = requests.post(url, data=jpg_to_bytes)
