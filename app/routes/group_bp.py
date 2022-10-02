from flask import Blueprint
from controllers.GroupController import index, store, show, update, delete

group_bp = Blueprint('group_bp', __name__)

group_bp.route('/', methods=['GET'])(index)

group_bp.route('/create', methods=['POST'])(store)

group_bp.route('/<int:group_id>', methods=['GET'])(show)

group_bp.route('/<int:group_id>/edit', methods=['POST'])(update)

group_bp.route('/<int:group_id>', methods=['DELETE'])(delete)
