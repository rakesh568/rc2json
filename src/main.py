import json
import os
from google.cloud import vision
vision_client = vision.ImageAnnotatorClient()

project_id = os.environ['GCP_PROJECT']
with open('config.json') as f:
    data = f.read()
config = json.loads(data)

def detect_text(filename):
    print('Looking for text in image {}'.format(filename))
    detect_text(args.path)