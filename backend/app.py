from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

products = [
    {"id": 1, "name": "Laptop", "price": 15000, "stock": 10},
    {"id": 2, "name": "Mouse", "price": 250, "stock": 50},
    {"id": 3, "name": "Keyboard", "price": 500, "stock": 30},
    {"id": 4, "name": "Monitor", "price": 8000, "stock": 15},
]

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    product = next((p for p in products if p['id'] == id), None)
    if product:
        return jsonify(product)
    return jsonify({"error": "Ürün bulunamadı"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)