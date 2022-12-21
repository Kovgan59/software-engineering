from flask import render_template, url_for, request, redirect
from flask import Flask
from PIL import Image
import numpy as np
import cv2
import io
import base64
from img_to_gcode import gcodes_start


app = Flask(__name__)

@app.route("/")
def main_page():    
    return render_template('index.html')


@app.route("/upload", methods=['POST'])
def upload_file():
    req = request
    img = req.files.get('file')
    if img.filename == '':
        return redirect(url_for('main_page'))
    img = np.asarray(bytearray(img.read()), dtype=np.uint8)
    img = cv2.imdecode(img, cv2.IMREAD_COLOR)   
    retval, buffer = cv2.imencode('.png', img)
    img_str = base64.b64encode(buffer)
    img_str = str(img_str)[2:-1]
    text, export_img = gcodes_start(img)
    if export_img == []:
        return render_template('result.html', success_flag=False, image=img_str, text=text)
    retval, buffer = cv2.imencode('.png', export_img)
    export_img_str = base64.b64encode(buffer)
    export_img_str = str(export_img_str)[2:-1]
    return render_template('result.html', success_flag=True, image=img_str, image2=export_img_str, text = text)
  

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
    