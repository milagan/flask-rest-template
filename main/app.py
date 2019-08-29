from flask import jsonify, request, Response, json

from main.settings import *

books = [
    {
        'name': 'Book 1',
        'price': 1.00,
        'isbn': 12345
    },
    {
        'name': 'Book 2',
        'price': 2.95,
        'isbn': 56789
    }
]


@app.route('/books')
def get_books():
    return jsonify({'books': books})


@app.route('/books/<int:isbn>')
def get_book_by_isbn(isbn):
    return_value = {}
    for book in books:
        if book['isbn'] == isbn:
            return_value = {
                'name': book['name'],
                'price': book['price']
            }
    return jsonify(return_value)


@app.route('/books', methods=['POST'])
def add_book():
    request_data = request.get_json()
    if valid_book_object(request_data):
        new_book = {
            'name': request_data['name'],
            'price': request_data['price'],
            'isbn': request_data['isbn']
        }
        books.insert(0, new_book)
        response = Response('', 201, mimetype='application/json')
        response.headers['Location'] = '/books/' + str(new_book['isbn'])
        return response
    else:
        invalid_book_object_error_msg = {
            'error': 'Invalid book object passed in request',
            'helpString': 'Data passed should contain name, price, and isbn fields'
        }
        response = Response(json.dumps(invalid_book_object_error_msg), 400, mimetype='application/json')
        return response


@app.route('/books/<int:isbn>', methods=['PUT'])
def replace_book(isbn):
    request_data = request.get_json()
    if not valid_put_request_data(request_data):
        invalid_book_object_err_msg = {
            "error": "Valid book object must be passed in the request",
            "helpString": "Data passed in similar to this {'name': 'bookname', 'price' :7.99}"
        }
        response = Response(json.dumps(invalid_book_object_err_msg), status=400, mimetype='application/json')
        return response

    new_book = {
        'name': request_data['name'],
        'price': request_data['price'],
        'isbn': isbn
    }
    i = 0
    for book in books:
        current_isbn = book['isbn']
        if current_isbn == isbn:
            books[i] = new_book
        i += 1
    response = Response("", status=204)
    return response


@app.route('/books/<int:isbn>', methods=['PATCH'])
def update_book(isbn):
    request_data = request.get_json()
    updated_book = {}
    if 'name' in request_data:
        updated_book['name'] = request_data['name']
    if 'price' in request_data:
        updated_book['price'] = request_data['price']
    for book in books:
        if book['isbn'] == isbn:
            book.update(updated_book)
    response = Response("", status=204)
    response.headers['Location'] = '/books' + str(isbn)
    return response


@app.route('/books/<int:isbn>', methods=['DELETE'])
def delete_book(isbn):
    i = 0
    for book in books:
        if book['isbn'] == isbn:
            books.pop(i)
            response = Response("", status=204)
            return response
        i += 1
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


if __name__ == '__main__':
    app.run()
