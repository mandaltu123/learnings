import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
books = [
    {'id': 1,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 2,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 3,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"


@app.route('/api/v1/resource/books/all', methods=['GET'])
def api_all():
    return jsonify(books)


@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    # check if the id was provided as part of the request
    # if id was present, assign it to a variable
    # iterate ove the list of books and find out particular book based on the passed id
    # else return error
    if 'bookid' in request.args:
        bookid = int(request.args['bookid'])
        print(f"id found from the request is {bookid}")
    else:
        return "bookid not present in the request parameter"
    # Create an empty list for results
    result = []
    # loop through the books and find the book for the given id
    for book in books:
        if book['id'] == bookid:
            result.append(book)
    if len(result) > 0:
        return jsonify(result)
    else:
        return "No book found for the given id"


app.run()
