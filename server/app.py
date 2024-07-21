from flask import Flask, request
import io
import base64
from PIL import Image, ImageCms

app = Flask(__name__)

@app.get('/options')
def options():
  return {
    'width': 40,
    'height': 40,
    'pixelsPerCell': 20,
  }

@app.post('/save')
def save():
  try:
    data: object = request.json
    data_url_string: str = data['dataURL'].split(',')[1]
    data_url_bytes = io.BytesIO(base64.decodebytes(bytes(data_url_string, "utf-8")))
    img = Image.open(data_url_bytes)
    
    # get pixel values
    width, height = img.size
    
    # every 20 pixels is a cell
    pixels_per_cell = 20

    # create new image
    new_img = Image.new('RGBA', (width // pixels_per_cell, height // pixels_per_cell), (255, 0, 0, 0))
    new_img_pixels = new_img.load()
    for x in range(0, width, pixels_per_cell):
      for y in range(0, height, pixels_per_cell):
        r, g, b, a = img.getpixel((x, y))
        # if alpha is 0 dont draw
        if a == 0:
          continue
        new_img_pixels[x // pixels_per_cell, y // pixels_per_cell] = (r, g, b)

    alpha_values = [1 if alpha > 128 else 0 for _, _, _, alpha in new_img.getdata()]

    print(alpha_values)

    return {
      'message': 'Image saved successfully',
    }
  except Exception as e:
    return {
      'message': 'Error saving image',
      'error': str(e),
    }

if __name__ == '__main__':
  app.run(debug=True)