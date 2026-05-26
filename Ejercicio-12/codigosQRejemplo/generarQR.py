import barcode
from barcode.writer import ImageWriter
import os

# Tu lista de productos
productos = [
    {"id": "E-001", "nombre": "Smartphone Pro Max 256GB"},
    {"id": "R-042", "nombre": "Camiseta Algodón Orgánico"},
    {"id": "A-102", "nombre": "Café de Especialidad 500g"},
    {"id": "E-015", "nombre": "Auriculares Noise Cancelling"},
    {"id": "H-009", "nombre": "Lámpara de Escritorio LED"},
    {"id": "H-021", "nombre": "Set de Cuchillos Cocina"},
    {"id": "R-101", "nombre": "Pantalon Denim Ajustado"},
    {"id": "123456789012", "nombre": "Chaqueta Cortavientos"},
    {"id": "7509876543219", "nombre": "Gorra Deportiva Negra"},
    {"id": "A-005", "nombre": "Te Verde Matcha Organic"},
    {"id": "TEST-BAR-POS", "nombre": "Caja Sorpresa Gourmet"},
    {"id": "H-055", "nombre": "Mesa de Centro Nogal"},
    {"id": "314159265358", "nombre": "Florero Ceramica Minimal"}
]
productos = [
    # Electrónica
    {"id": "E-001", "nombre": "Smartphone Pro Max 256GB"},
    {"id": "E-015", "nombre": "Auriculares Noise Cancelling"},
    {"id": "9781234567897", "nombre": "E-Reader Paperwhite",}, # EAN-13
    {"id": "8431234567890", "nombre": "Altavoz Bluetooth Portátil"}, # EAN-13

    # Ropa
    {"id": "R-042", "nombre": "Camiseta Algodón Orgánico"},
    {"id": "R-101", "nombre": "Pantalón Denim Ajustado"},
    {"id": "123456789012", "nombre": "Chaqueta Cortavientos"}, # UPC-A
    {"id": "7509876543219", "nombre": "Gorra Deportiva Negra"}, # EAN-13

    # Alimentos
    {"id": "A-102", "nombre": "Café de Especialidad 500g"},
    {"id": "A-005", "nombre": "Té Verde Matcha Organic"},

    # Hogar
    {"id": "H-009", "nombre": "Lámpara de Escritorio LED"},
    {"id": "H-021", "nombre": "Set de Cuchillos Cocina"},
    {"id": "H-055", "nombre": "Mesa de Centro Nogal"},
    {"id": "3141592653589", "nombre": "Florero Cerámica Minimal"} # EAN-13 (Pi)
]

# Ruta específica
ruta_destino = r"c:\Users\juanl\OneDrive\Escritorio\Lab-de-introduccion-a-la-programacion\Ejercicio-12\codigosQRejemplo"

if not os.path.exists(ruta_destino):
    os.makedirs(ruta_destino)

# Configuración del formato de código de barras
# Code128 es el más versátil para SKUs alfanuméricos
CODIGO_BAR_TIPO = barcode.get_barcode_class('code128')

for p in productos:
    sku = p["id"]
    nombre_seguro = "".join([c for c in p["nombre"] if c.isalnum() or c==' ']).rstrip().replace(" ", "_")
    
    # Crear el código de barras
    # Usamos ImageWriter para que se guarde como PNG
    codigo = CODIGO_BAR_TIPO(sku, writer=ImageWriter())
    
    # Nombre del archivo (la librería añade automáticamente .png)
    nombre_archivo = f"bar_{sku}_{nombre_seguro}"
    ruta_completa = os.path.join(ruta_destino, nombre_archivo)
    
    # Guardar (le pasamos la ruta sin la extensión .png)
    codigo.save(ruta_completa)
    print(f"Generado código de barras: {nombre_archivo}.png")

print(f"\n¡Listo!")