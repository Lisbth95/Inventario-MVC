from flask import Blueprint, render_template, request, redirect, url_for
from models.supplier import Supplier
from database import dbConnection

db = dbConnection()
supplier_bp = Blueprint('supplier_bp', __name__, url_prefix='/suppliers')

@supplier_bp.route('/', methods=['GET'])
def home_suppliers():
    suppliers = db['suppliers'].find()
    return render_template('suppliers.html', suppliers=suppliers)

@supplier_bp.route('/', methods=['POST'])
def addsuppliers():
    suppliers = db['suppliers']
    nombre = request.form['nombre']
    apellidoP = request.form['apellidoP']
    apellidoM = request.form['apellidoM']
    direccion = request.form['direccion']
    celular = request.form['celular']
    nota = request.form['nota']

    supplier = Supplier(nombre, apellidoP, apellidoM, direccion, celular, nota)
    suppliers.insert_one(supplier.toDBCollection())
    return redirect(url_for('supplier_bp.home_suppliers'))

@supplier_bp.route('/delete_supplier/<string:supplier_name>')
def delete_supplier(supplier_name):
    db['suppliers'].delete_one({'nombre' : supplier_name})
    return redirect(url_for('supplier_bp.home_suppliers'))

@supplier_bp.route('/edit_supplier/<string:supplier_name>', methods=['POST'])
def edit_supplier(supplier_name):
    data = {
        'nombre': request.form['nombre'],
        'apellidoP': request.form['apellidoP'],
        'apellidoM': request.form['apellidoM'],
        'direccion': request.form['direccion'],
        'celular': request.form['celular'],
        'nota': request.form['nota'],
    }
    db['suppliers'].update_one({'nombre':supplier_name}, {'$set': data})
    return redirect(url_for('supplier_bp.home_suppliers'))
 