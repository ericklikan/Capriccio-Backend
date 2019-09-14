#!/usr/bin/env python
from flask import Blueprint, session, request, Flask, flash, request, redirect, url_for, send_from_directory
from flask import current_app as app
from werkzeug.utils import secure_filename
import os, json

api = Blueprint('api', __name__)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@api.route("/test", methods=["POST",'GET'])
def test():
    if request.method == 'GET':
        return 'api test'
    if request.method == 'POST':
        print(request.json)
        return json.dumps(request.json)
