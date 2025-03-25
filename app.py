from flask import Flask, render_template
from database import dbConnection

from controllers.customerController import customer_bp
from controllers.productController import product_bp
from controllers.supplierController import supplier_bp

app = Flask(__name__)
db = dbConnection()

# Rutas principales
@app.route('/')
def index():
    return render_template('index.html')

# Registrar blueprints
app.register_blueprint(product_bp)
app.register_blueprint(customer_bp)
app.register_blueprint(supplier_bp)

if __name__ == '__main__':
    app.run(debug=True, port=4000)
