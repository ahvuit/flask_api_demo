from flask import jsonify


class BaseResponse:
    def __init__(self, message="", data=None, code=None):
        self.message = message
        self.data = data
        self.code = code

    def to_dict(self):
        return jsonify({'data': self.data, 'message': self.message, 'code': self.code})
