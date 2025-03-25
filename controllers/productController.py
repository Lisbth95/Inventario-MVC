from flask import Blueprint, render_template, request, redirect, url_for
from models.product import Product
from database import dbConnection

db = dbConnection()
product_bp = Blueprint('product_bp', __name__, url_prefix='/products')

@product_bp.route('/', methods=['GET'])
def home_products():
    products = db['products'].find()
    return render_template('products.html', products=products)

#metodo post
@product_bp.route('/', methods=['POST'])
def addProducts():
    products = db['products']
    nombre = request.form['nombre']
    precio = request.form['precio']
    cantidad = request.form['cantidad']
    product = Product(nombre, precio, cantidad)
    products.insert_one(product.toDBCollection())
    return redirect(url_for('product_bp.home_products'))
    
#method delete 
@product_bp.route('/delete_product/<string:product_name>')
def delete_product(product_name):
    db['products'].delete_one({'nombre' : product_name})
    return redirect(url_for('product_bp.home_products'))

#method Put
@product_bp.route('/edit_product/<string:product_name>', methods=['POST'])
def edit_product(product_name):
    data = {
        'nombre': request.form['nombre'],
        'precio': request.form['precio'],
        'cantidad': request.form['cantidad'],
    }

    db['products'].update_one({'nombre':product_name}, {'$set': data})
    return redirect(url_for('product_bp.home_products'))
