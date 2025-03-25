from flask import Blueprint, render_template, request, redirect, url_for
from models.customers import Customer
from database import dbConnection

db = dbConnection()
customer_bp = Blueprint('customer_bp', __name__, url_prefix='/customers')

@customer_bp.route('/', methods=['GET'])
def home_customers():
    customers = db['customers'].find()
    return render_template('customers.html', customers=customers)

#metodo post
@customer_bp.route('/', methods=['POST'])
def addcustomers():
    customers = db['customers']
    nombre = request.form['nombre']
    apellidoP = request.form['apellidoP']
    apellidoM = request.form['apellidoM']
    direccion = request.form['direccion']
    celular = request.form['celular']
    nota = request.form['nota']
    
    customer = Customer(nombre, apellidoP, apellidoM, direccion, celular, nota)
    customers.insert_one(customer.toDBCollection())
    return redirect(url_for('customer_bp.home_customers'))

#method delete 
@customer_bp.route('/delete_customer/<string:customer_name>')
def delete_customer(customer_name):
    db['customers'].delete_one({'nombre' : customer_name})
    return redirect(url_for('customer_bp.home_customers'))

#method Put
@customer_bp.route('/edit_customer/<string:customer_name>', methods=['POST'])
def edit_customer(customer_name):
    data = {
        'nombre': request.form['nombre'],
        'apellidoP': request.form['apellidoP'],
        'apellidoM': request.form['apellidoM'],
        'direccion': request.form['direccion'],
        'celular': request.form['celular'],
        'nota': request.form['nota'],
    }
    db['customers'].update_one({'nombre':customer_name}, {'$set': data})
    return redirect(url_for('customer_bp.home_customers'))
