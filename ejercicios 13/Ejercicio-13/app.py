from flask import Flask, request, jsonify, render_template
import cv2
import numpy as np
import sqlite3
import base64
from pyzbar.pyzbar import decode

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('inventario.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS productos 
                      (id_producto TEXT PRIMARY KEY, nombre TEXT, codigo TEXT, num_producto INTEGER)''')
    conn.commit()
    conn.close()

# --- ESTA ES LA RUTA QUE FALTABA ---
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/procesar', methods=['POST'])
def procesar():
    try:
        data = request.json
        img_data = base64.b64decode(data['image'].split(',')[1])
        nparr = np.frombuffer(img_data, np.uint8)
        frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        objetos_detectados = decode(gray)
        
        codigo_detectado = ""
        for obj in objetos_detectados:
            codigo_detectado = obj.data.decode('utf-8')

        return jsonify({"codigo": codigo_detectado})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/guardar', methods=['POST'])
def guardar():
    try:
        d = request.json
        conn = sqlite3.connect('inventario.db')
        curr = conn.cursor()
        curr.execute("INSERT INTO productos VALUES (?,?,?,?)", 
                     (d['id_p'], d['nom'], d['cod'], d['num_p']))
        conn.commit()
        conn.close()
        return jsonify({"status": "ok"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/obtener_productos', methods=['GET'])
def obtener_productos():
    try:
        conn = sqlite3.connect('inventario.db')
        conn.row_factory = sqlite3.Row  # Esto permite leer por nombre de columna
        curr = conn.cursor()
        curr.execute("SELECT * FROM productos")
        rows = curr.fetchall()
        
        # Convertir los resultados a una lista de diccionarios
        productos = [dict(row) for row in rows]
        conn.close()
        return jsonify(productos)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/eliminar/<id_p>', methods=['DELETE'])
def eliminar(id_p):
    try:
        conn = sqlite3.connect('inventario.db')
        curr = conn.cursor()
        # Borramos el registro que coincida con el ID
        curr.execute("DELETE FROM productos WHERE id_producto = ?", (id_p,))
        conn.commit()
        conn.close()
        return jsonify({"status": "ok"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)