#!/usr/bin/env python
from flask import Blueprint, session, request, Flask, flash, request, redirect, url_for, send_from_directory
from flask import current_app as app
from werkzeug.utils import secure_filename
import os
import json
import uuid
import base64

from .staffRecognizer import generateMidiFileFromImage

api = Blueprint('api', __name__)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower(
           ) in app.config['ALLOWED_EXTENSIONS']


@api.route("/test", methods=["POST", 'GET'])
def test():
    if request.method == 'GET':
        return 'api test'
    if request.method == 'POST':
        return json.dumps(request.json)


@api.route("/image", methods=["POST"])
def image():
    # Create folder if not exist
    if not os.path.isdir(os.path.join(app.root_path, app.config["UPLOAD_FOLDER"])):
        os.mkdir(os.path.join(app.root_path, app.config["UPLOAD_FOLDER"]))

    decoded_string = base64.b64decode(str.encode(request.json['image']))
    id = uuid.uuid4()
    # print("image id: {}".format(id))
    filename = secure_filename("{}.jpeg".format(id))
    filePath = os.path.join(
        app.root_path, app.config["UPLOAD_FOLDER"], filename)
    with open(filePath, "wb") as image_file:
        image_file.write(decoded_string)

    # Run opencv
    generateMidiFileFromImage(id, filePath)

    return json.dumps({"fileName": "{}.mid".format(id)})


@api.route("/process_images", methods=["GET"])
def process_images():
    # print(request.args.get("images"))
    return ""


@api.route('/get_image/<path:filename>')
def uploaded_file(filename):
    uploads = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'])
    return send_from_directory(uploads, filename, as_attachment=True)


@api.route('/delete_image/<path:filename>', methods=['DELETE'])
def delete_file(filename):
    uploads = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'])
    os.remove(os.path.join(uploads, filename))
    return "OK"
