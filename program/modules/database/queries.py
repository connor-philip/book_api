from book_api.modules.database.db_connection import bookdb as bookdb


def get_book_dict_by_id(_id):
    return bookdb.books.find_one({"_id": _id})


def get_all_books():
    return bookdb.books.find({})


def get_authors():
    authorList = []
    cursor = bookdb.books.find({}, {"authors": 1, "_id": 0})

    for item in cursor:
        print(item)
        if isinstance(item["authors"], list):
            for author in item["authors"]:
                if author not in authorList:
                    authorList.append(author)

    return authorList


def get_genres():
    genreList = []
    cursor = bookdb.books.find({}, {"genres": 1, "_id": 0})

    for item in cursor:
        if isinstance(item["genres"], list):
            for genre in item["genres"]:
                if genre not in genreList:
                    genreList.append(genre)

    return genreList
