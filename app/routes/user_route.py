from flask import Blueprint, jsonify, request, make_response, json

from app.models.base_response import BaseResponse
from app.models.user import User
from app.services.user_service import get_user, create_user

user_bp = Blueprint('user', __name__, url_prefix='/user')


@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user_route(user_id):
    try:
        user = get_user(user_id)
        if user:
            return BaseResponse(message="Success", data=[user.to_dict()], code=200).to_dict(), 200
        else:
            return BaseResponse(message="User not found", data=None, code=404).to_dict(), 404
    except Exception as e:
        print(e)
        return BaseResponse(message="Server Error", data=None, code=500).to_dict(), 500


@user_bp.route('/', methods=['POST'])
def create_user_route():
    try:
        data = request.get_json()
        new_user = create_user(data['username'], data['email'])
        return BaseResponse(message="Success", data=[new_user.to_dict()], code=200).to_dict(), 200
    except Exception as e:
        print(e)
        return BaseResponse(message="Server Error", data=None, code=500).to_dict(), 500

