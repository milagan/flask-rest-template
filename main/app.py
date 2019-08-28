from flask import Flask, jsonify, request, Response, json

app = Flask(__name__)

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


def valid_book_object(book_object):
    if 'name' in book_object and 'price' in book_object and 'isbn' in book_object:
        return True
    else:
        return False


if __name__ == '__main__':
    app.run()
