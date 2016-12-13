from flask import Blueprint, jsonify

bp = Blueprint('root', __name__)

@bp.route('/root', methods=['GET'])
def profile():
    return jsonify({'me': 'foo', 'msg': 'hello'})
