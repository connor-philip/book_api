from flask import Flask, jsonify, render_template
import book_api.modules.database.queries as queries
app = Flask("book_api_app")


@app.route("/", methods=['GET'])
@app.route("/api/", methods=['GET'])
@app.route("/home/", methods=['GET'])
def home():
    return render_template("home_template.html")


@app.route("/api/books/", methods=['GET'])
def get_books():
    cursorObject = queries.get_all_books()
    booksJson = jsonify(list(cursorObject))

    return booksJson


@app.route("/api/authors/", methods=['GET'])
def get_authors():
    cursorObject = queries.get_authors()
    authorsJson = jsonify(list(cursorObject))

    return authorsJson


@app.route("/api/genres/", methods=['GET'])
def get_genres():
    cursorObject = queries.get_genres()
    genresJson = jsonify(list(cursorObject))

    return genresJson
