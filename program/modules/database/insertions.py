from book_api.modules.database.db_connection import bookdb as bookdb
from book_api.modules.database.queries import get_book_dict_by_id
import book_api.modules.ba_logging.message_formatters as mf
import book_api.modules.ba_logging.log_controller as lc
import hashlib


class AddBook:

    def __init__(self, title, authors, genres=[], tags=[], isbn10="", isbn13=""):
        self.success = False
        self.bookId = None
        self.message = None

        self.logger = lc.get_logger("databaseModuleLogger")

        valid = self.check_if_book_dict_has_valid_values(title,
                                                         authors,
                                                         genres,
                                                         tags,
                                                         isbn10,
                                                         isbn13)

        if valid:
            self.bookId = self.create_book_id(title, isbn10, isbn13)
            bookDict = self.create_book_dict(self.bookId,
                                             title,
                                             authors,
                                             genres,
                                             tags,
                                             isbn10,
                                             isbn13)
            self.add_book_to_db(bookDict)

    def __del__(self):
        lc.close_log(self.logger)

    def check_if_book_dict_has_valid_values(self, title, authors, genres=[], tags=[], isbn10="", isbn13=""):
        errorMessage = ""

        # Check parameter types
        for strParam in [title, isbn10, isbn13]:
            if isinstance(strParam, str) is False:
                errorMessageLine = mf.format_type_error_message(strParam, "str", strParam)
                errorMessage = "{}\n{}".format(errorMessage, errorMessageLine)

        for listParam in [genres, authors, tags]:
            if isinstance(listParam, list):
                for strItem in listParam:
                    if isinstance(strItem, str) is False:
                        description = "{} list item".format(listParam)
                        errorMessageLine = mf.format_type_error_message(description, "str", strItem)
                        errorMessage = "{}\n{}".format(errorMessage, errorMessageLine)
            else:
                errorMessageLine = mf.format_type_error_message(listParam, "list", listParam)
                errorMessage = "{}\n{}".format(errorMessage, errorMessageLine)

        # Ensure ISBN have correct length
        if isbn10 and len(isbn10) != 10:
            errorMessageLine = mf.unexpected_length_error_message("ISBN10", "10", isbn10)
            errorMessage = "{}\n{}".format(errorMessage, errorMessageLine)
        if isbn13 and len(isbn13) != 13:
            errorMessageLine = mf.unexpected_length_error_message("ISBN13", "13", isbn13)
            errorMessage = "{}\n{}".format(errorMessage, errorMessageLine)

        # If error message is empty return True
        if errorMessage:
            self.message = errorMessage
            self.logger.info(errorMessage)
            return False
        else:
            return True

    def create_book_id(self, title, isbn10="", isbn13=""):
        joinedString = title + isbn10 + isbn13
        encodedString = joinedString.encode("utf-8")

        return hashlib.md5(encodedString).hexdigest()

    def create_book_dict(self, bookId, title, authors, genres=[], tags=[], isbn10="", isbn13=""):
        bookDict = {
            "_id": bookId,
            "title": title,
            "authors": authors,
            "genres": genres,
            "tags": tags,
            "isbn10": isbn10,
            "isbn13": isbn13
        }

        return bookDict

    def add_book_to_db(self, bookDict):
        if get_book_dict_by_id(bookDict["_id"]) is None:
            bookdb.books.insert_one(bookDict)
            self.message = "Book added successfully"
            self.success = True
        else:
            self.message = "Tried to add id {} to db but it already exists".format(bookDict["_id"])
            self.logger.info(self.message)
            self.success = False

        return self.success
