from flask import jsonify, request
from app.api import bp
import json


@bp.route('/update_model', methods=['POST'])
def update_model():
    data = request.get_json() or {}
    respdata = {'success': True}
    response = jsonify(respdata)
    response.status_code = 200
    return response

def get_bytes_from_file(filename):
    return open(filename, "rb").read()
