from flask import g, Blueprint, request, abort, url_for, jsonify

main = Blueprint('main', __name__)

@main.route('/')
def index():
  return "Welcome!"