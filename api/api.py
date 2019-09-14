#!/usr/bin/env python
from flask import Blueprint, session, request, Flask, flash, request, redirect, url_for, send_from_directory
from flask import current_app as app
from werkzeug.utils import secure_filename
import os, json, uuid, base64

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

@api.route("/image", methods=["POST"])
def image():
    if not os.path.isdir(app.config["UPLOAD_FOLDER"]):
        os.mkdir(app.config["UPLOAD_FOLDER"])
    encoded_string = base64.b64encode(request.json['image'])
    decoded_string = base64.b64decode(encoded_string)   
    filename = secure_filename("{}.jpeg".format(uuid.uuid4()))
    with open(os.path.join(app.config["UPLOAD_FOLDER"], filename), "wb") as image_file:
        image_file.write(decoded_string)
    return filename

@api.route('/get_image/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)