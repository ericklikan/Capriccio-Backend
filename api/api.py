#!/usr/bin/env python
from flask import Blueprint, session, request

api = Blueprint('api', __name__)


@api.route("/test")
def test():
    return 'api test'
