from flask import Flask, render_template, request, jsonify
import cv2
import numpy as np
import base64
from pyzbar.pyzbar import decode

app = Flask(__name__)

# Catálogo de productos basado en tus diseños
productos = [
    {"id": "E-001", "nombre": "Smartphone Pro Max 256GB", "cat": "Electrónica", "precio": 1299.99, "oferta": False},
    {"id": "R-042", "nombre": "Camiseta Algodón Orgánico", "cat": "Ropa", "precio": 25.50, "oferta": True},
    {"id": "A-102", "nombre": "Café de Especialidad 500g", "cat": "Alimentos", "precio": 18.20, "oferta": False},
    {"id": "E-015", "nombre": "Auriculares Noise Cancelling", "cat": "Electrónica", "precio": 349.00, "oferta": True},
    {"id": "H-009", "nombre": "Lámpara de Escritorio LED", "cat": "Hogar", "precio": 45.00, "oferta": False},
    {"id": "H-021", "nombre": "Set de Cuchillos Cocina", "cat": "Hogar", "precio": 89.99, "oferta": False},

    # Electrónica
    {"id": "E-001", "nombre": "Smartphone Pro Max 256GB", "cat": "Electrónica", "precio": 1299.99, "oferta": False},
    {"id": "E-015", "nombre": "Auriculares Noise Cancelling", "cat": "Electrónica", "precio": 349.00, "oferta": True},
    {"id": "9781234567897", "nombre": "E-Reader Paperwhite", "cat": "Electrónica", "precio": 149.50, "oferta": False}, # EAN-13
    {"id": "8431234567890", "nombre": "Altavoz Bluetooth Portátil", "cat": "Electrónica", "precio": 79.99, "oferta": False}, # EAN-13

    # Ropa
    {"id": "R-042", "nombre": "Camiseta Algodón Orgánico", "cat": "Ropa", "precio": 25.50, "oferta": True},
    {"id": "R-101", "nombre": "Pantalón Denim Ajustado", "cat": "Ropa", "precio": 55.00, "oferta": False},
    {"id": "123456789012", "nombre": "Chaqueta Cortavientos", "cat": "Ropa", "precio": 89.95, "oferta": False}, # UPC-A
    {"id": "7509876543219", "nombre": "Gorra Deportiva Negra", "cat": "Ropa", "precio": 19.99, "oferta": True}, # EAN-13

    # Alimentos
    {"id": "A-102", "nombre": "Café de Especialidad 500g", "cat": "Alimentos", "precio": 18.20, "oferta": False},
    {"id": "A-005", "nombre": "Té Verde Matcha Organic", "cat": "Alimentos", "precio": 29.90, "oferta": False},
    {"id": "TEST-QR-SPECIAL", "nombre": "Caja Sorpresa Gourmet (QR)", "cat": "Alimentos", "precio": 45.00, "oferta": True}, # Para prueba QR

    # Hogar
    {"id": "H-009", "nombre": "Lámpara de Escritorio LED", "cat": "Hogar", "precio": 45.00, "oferta": False},
    {"id": "H-021", "nombre": "Set de Cuchillos Cocina", "cat": "Hogar", "precio": 89.99, "oferta": False},
    {"id": "H-055", "nombre": "Mesa de Centro Nogal", "cat": "Hogar", "precio": 199.00, "oferta": True},
    {"id": "3141592653589", "nombre": "Florero Cerámica Minimal", "cat": "Hogar", "precio": 34.50, "oferta": False} # EAN-13 (Pi)

]

@app.route('/')
def index():
    return render_template('index.html', productos=productos)

@app.route('/scanner', methods=['POST'])
def scanner():
    try:
        data = request.json['image']
        img_data = base64.b64decode(data.split(',')[1])
        nparr = np.frombuffer(img_data, np.uint8)
        frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        objetos = decode(frame)
        
        if objetos:
            for obj in objetos:
                codigo_leido = obj.data.decode('utf-8')
                # Buscar si el código existe en el catálogo
                prod = next((p for p in productos if p['id'] == codigo_leido), None)
                
                print(f"Detectado: {codigo_leido}")
                return jsonify({
                    "status": "ok", 
                    "value": codigo_leido, 
                    "producto": prod
                })
    except Exception as e:
        print(f"Error en servidor: {e}")

    return jsonify({"status": "none"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)