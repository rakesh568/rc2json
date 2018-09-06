import json
import os
from google.cloud import vision
import io
vision_client = vision.ImageAnnotatorClient()

# project_id = os.environ['GCP_PROJECT']
with open('config.json') as f:
    data = f.read()
config = json.loads(data)


def detect_text(path):
    """Detects text in the file."""
    client = vision.ImageAnnotatorClient()

    # [START vision_python_migration_text_detection]
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')

    for text in texts:
        print('\n"{}"'.format(text.description))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])

        print('bounds: {}'.format(','.join(vertices)))

detect_text('/Users/acko094/Downloads/rc.jpg')