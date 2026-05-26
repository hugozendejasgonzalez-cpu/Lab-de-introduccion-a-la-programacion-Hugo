from flask import Flask, render_template, request, jsonify
import cv2
import numpy as np
import base64
from pyzbar.pyzbar import decode

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scanner', methods=['POST'])
def scanner():

    data = request.json['image']

    img_data = base64.b64decode(data.split(',')[1])
    
    nparr = np.frombuffer(img_data, np.uint8)
    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    objetos = decode(frame)
    
    if objetos:
        for obj in objetos:
            resultado = obj.data.decode('utf-8')
            tipo = obj.type
            print(f"Detectado: {resultado} ({tipo})")
            return jsonify({"status": "ok", "value": resultado, "type": tipo})

    return jsonify({"status": "none"})

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000, debug=True)