from flask import Flask, jsonify, request

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
    return jsonify(request.get_json())


def valid_book_object(book_object):
    if 'name' in book_object and 'price' in book_object and 'isbn' in book_object:
        return True
    else:
        return False


if __name__ == '__main__':
    app.run()
