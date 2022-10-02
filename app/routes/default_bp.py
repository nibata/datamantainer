from flask import Blueprint
from controllers.DefaultController import index

default_bp = Blueprint("default_bp", __name__)

default_bp.route("/", methods=["GET"])(index)