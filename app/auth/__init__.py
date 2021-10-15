from flask import Blueprint
from app.auth import controllers


bp = Blueprint('auth', __name__)

@bp.route('/login', methods=['POST'])
def login():
    return controllers.get_access()
