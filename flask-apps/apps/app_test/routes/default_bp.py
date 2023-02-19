from flask import Blueprint
from ..controllers.DefaultController import index, sentry_test, register_test_job

default_bp = Blueprint("default_bp", __name__)

default_bp.route("/", methods=["GET"])(index)

default_bp.route("/sentry_test", methods=["GET"])(sentry_test)

default_bp.route("/register_job", methods=["GET"])(register_test_job)
