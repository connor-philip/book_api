from book_api.modules.database.db_connection import bookdb as bookdb


def get_book_dict_by_id(_id):
    return bookdb.books.find_one({"_id": _id})


def get_all_books():
    return bookdb.books.find({}).sort([("_id", 1)])


def get_all_authors():
    authorList = []
    cursor = bookdb.books.find({}, {"authors": 1, "_id": 0}).sort([("_id", 1)])

    for item in cursor:
        if isinstance(item["authors"], list):
            for author in item["authors"]:
                if author not in authorList:
                    authorList.append(author)

    return authorList


def get_books_by_author(author):
    return bookdb.books.find({"authors": author}, {"title": 1, "_id": 1}).sort([("_id", 1)])


def get_all_genres():
    genreList = []
    cursor = bookdb.books.find({}, {"genres": 1, "_id": 0}).sort([("_id", 1)])

    for item in cursor:
        if isinstance(item["genres"], list):
            for genre in item["genres"]:
                if genre not in genreList:
                    genreList.append(genre)

    return genreList


def get_books_in_genre(genre):
    return bookdb.books.find({"genres": genre}, {"title": 1, "_id": 1}).sort([("_id", 1)])
