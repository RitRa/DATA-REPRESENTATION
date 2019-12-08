# export FLASK_APP=a_simpleserver.py
#  python -m flask run
# use week 5 as a reference
from flask import Flask, jsonify,  request, abort, make_response
app = Flask(__name__, static_url_path='', static_folder='.')

books=[{"id":1, "Title": "Harry Potter", "Author": "JK", "Price": 1000},
{"id":2, "Title": "The Quiet American", "Author": "Greene", "Price": 800},
{"id":3, "Title": "Something Steamy", "Author": "Jackie Collins", "Price": 1100}]

NextId = 4
#@app.route('/')
#def hello_world():
#    return 'Hello, World!'

# curl "http://127.0.0.1:5000/books/124"


@app.route('/books')

# curl "http://127.0.0.1:5000/books"
def getAll():
    return jsonify(books)

@app.route('/books/<int:id>')
def findById(id):
    foundBooks = list(filter(lambda b:b['id']==id, books))
    if len(foundBooks) == 0:
        return jsonify ({}) , 204
    return jsonify (foundBooks[0])

# curl -X POST  "http://127.0.0.1:5000/books"

## curl -i -H "Content-Type:application/json" -X PUT -d '{"Title": "Harry Potter2", "Author": "JK", "Price": 1000}' http://127.0.0.1:5000/books
@app.route('/books',methods=['POST'])
def create():
    global NextId
    if not request.json:
        abort(400)
    #other checking that it is correct formatted for more marks
    book = {
        "id": NextId,
        "Title": request.json['Title'],
         "Author": request.json['Author'],
          "Price": request.json['Price']
    }
    NextId += 1
    books.append(book)
    return jsonify(book)

    return "in create"

#curl -X PUT "http://127.0.0.1:5000/books/124"

# curl -i -H "Content-Type:application/json" -X PUT -d  '{ "Title":"me" }' http://127.0.0.1:5000/books/1
    
# curl -i -H "Content-Type:application/json" -X PUT -d  '{"Title":"ritt","Author":"Ruta", "Price":34 }' http://127.0.0.1:5000/books/1
@app.route('/books/<int:id>',methods=['PUT'])
def update(id):
    foundBooks = list(filter(lambda t:t['id']==id, books))
    if (len(foundBooks) == 0):
        abort(404)
    foundBook = foundBooks[0]
    if not request.json:
        abort(400)
    reqJson = request.json
    if "Title" in reqJson:
        foundBook["Title"] =reqJson['Title']
    if 'Author' in reqJson:
        foundBook['Author'] = reqJson['Author']
    if "Price" in reqJson:
        foundBook["Price"] =reqJson['Price']

    return jsonify(foundBook)



    return "in update for id" +str(id)

#  curl -X DELETE http://127.0.0.1:5000/books/1

@app.route('/books/<int:id>',methods=['DELETE'])
def delete(id):
    foundBooks = list(filter(lambda t:t['id']==id, books))
    if (len(foundBooks) == 0):
        abort(404)
    books.remove(foundBooks[0])
    return jsonify({"done":True})

    return "in delete for id" +str(id)

if __name__ == '__main__':
    app.run(debug=True)    