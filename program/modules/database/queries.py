from book_api.modules.database.db_connection import bookdb as bookdb


def get_book_dict_by_id(_id):
    return bookdb.books.find_one({"_id": _id})


def get_all_books():
    return bookdb.books.find({})
