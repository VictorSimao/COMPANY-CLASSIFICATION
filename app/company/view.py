import os

from flask import Blueprint, jsonify, request, render_template

from app.company.action import get_all as get_all_company, get_by_id as get_company_by_id, \
    update as update_company

app_company = Blueprint('app_company', __name__)


@app_company.route('/company', methods=['GET'])
def get() -> tuple:
    return jsonify([company for company in get_all_company()]), 200


@app_company.route('/company/<int:id>', methods=['GET'])
def get_by_id(id: int) -> tuple:
    company = get_company_by_id(id)
    return jsonify(company), 200


@app_company.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        company_id = request.form['cia']
        file = request.files['file']
        file.save(os.path.join('archive/upload', file.filename))
        update_company(company_id, file.filename)
    return render_template('home.html')
