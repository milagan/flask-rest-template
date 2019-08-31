import datetime
from functools import wraps

import jwt
from flask import jsonify, request, Response

from model.BookModel import *
from model.UserModel import *


def token_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = request.args.get('token')
        try:
            jwt.decode(token, key=app.config['SECRET_KEY'], algorithms=['HS256'])
            return f(*args, **kwargs)
        except:
            return jsonify({'error': 'Need a valid token to view this page'}), 401

    return wrapper


@app.route('/login', methods=['POST'])
def get_token():
    request_data = request.get_json()
    username = str(request_data['username'])
    password = str(request_data['password'])

    match = User.username_password_match(username, password)
    if match:
        expiration_date = datetime.datetime.utcnow() + datetime.timedelta(seconds=300)
        token = jwt.encode({'exp': expiration_date}, key=app.config['SECRET_KEY'], algorithm='HS256')
        return token
    else:
        return Response("", status=401, mimetype='application/json')


@app.route('/books')
@token_required
def get_books():
    return jsonify({'books': Book.get_all_books()})


@app.route('/books/<int:isbn>')
@token_required
def get_book_by_isbn(isbn):
    return_value = Book.get_book(isbn)
    return jsonify(return_value)


@app.route('/books', methods=['POST'])
@token_required
def add_book():
    request_data = request.get_json()
    if valid_book_object(request_data):
        Book.add_book(request_data['name'], request_data['price'], request_data['isbn'])
        response = Response('', 201, mimetype='application/json')
        response.headers['Location'] = '/books/' + str(request_data['isbn'])
        return response
    else:
        invalid_book_object_error_msg = {
            'error': 'Invalid book object passed in request',
            'helpString': 'Data passed should contain name, price, and isbn fields'
        }
        response = Response(json.dumps(invalid_book_object_error_msg), 400, mimetype='application/json')
        return response


@app.route('/books/<int:isbn>', methods=['PUT'])
@token_required
def replace_book(isbn):
    request_data = request.get_json()
    if not valid_put_request_data(request_data):
        invalid_book_object_err_msg = {
            "error": "Valid book object must be passed in the request",
            "helpString": "Data passed in similar to this {'name': 'bookname', 'price' :7.99}"
        }
        response = Response(json.dumps(invalid_book_object_err_msg), status=400, mimetype='application/json')
        return response

    Book.replace_book(isbn, request_data['name'], request_data['price'])
    response = Response("", status=204)
    return response


@app.route('/books/<int:isbn>', methods=['PATCH'])
@token_required
def update_book(isbn):
    request_data = request.get_json()
    if 'name' in request_data:
        Book.update_book_name(isbn, request_data['name'])
    if 'price' in request_data:
        Book.update_book_price(isbn, request_data['price'])

    response = Response("", status=204)
    response.headers['Location'] = '/books' + str(isbn)
    return response


@app.route('/books/<int:isbn>', methods=['DELETE'])
@token_required
def delete_book(isbn):
    if Book.delete_book(isbn):
        response = Response("", status=204)
        return response

    invalid_book_object_err_msg = {
        "error": "Books with the ISBN number provided was not found"
    }
    response = Response(json.dumps(invalid_book_object_err_msg), status=404)
    return response


def valid_book_object(book_object):
    if 'name' in book_object and 'price' in book_object and 'isbn' in book_object:
        return True
    else:
        return False


def valid_put_request_data(request_data):
    if 'name' in request_data and 'price' in request_data:
        return True
    else:
        return False


def create_app():
    return app


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
