from flask import Flask, jsonify, render_template, request
import book_api.modules.database.queries as queries
import book_api.modules.database.insertions as insertions
app = Flask("book_api_app")


@app.route("/", methods=["GET"])
@app.route("/api/", methods=["GET"])
@app.route("/home/", methods=["GET"])
def home():
    return render_template("home_template.html")


@app.route("/api/books/", methods=["GET"])
def get_books():
    cursorObject = queries.get_all_books()
    booksJson = jsonify(list(cursorObject))

    return booksJson


@app.route("/api/books/add_book", methods=["POST"])
def add_book():
    userJson = request.get_json()
    ab = insertions.AddBook(title=userJson["title"],
                            authors=userJson["authors"],
                            genres=userJson["genres"],
                            tags=userJson["tags"],
                            isbn10=userJson["isbn10"],
                            isbn13=userJson["isbn13"])

    bookDict = queries.get_book_dict_by_id(ab.bookId)

    returnJson = {
        "success": ab.success,
        "message": ab.message,
        "book_id": ab.bookId,
        "bookObject": bookDict
    }

    if ab.success is True:
        returnStatus = 201
    else:
        returnStatus = 400

    return (jsonify(returnJson), returnStatus)


@app.route("/api/books/<bookId>", methods=["GET"])
def get_book(bookId):
    bookDict = queries.get_book_dict_by_id(bookId)
    bookJson = jsonify(bookDict)

    return bookJson


@app.route("/api/authors/", methods=["GET"])
def get_authors():
    cursorObject = queries.get_all_authors()
    authorsJson = jsonify(list(cursorObject))

    return authorsJson


@app.route("/api/genres/", methods=["GET"])
def get_genres():
    cursorObject = queries.get_all_genres()
    genresJson = jsonify(list(cursorObject))

    return genresJson
