import unittest
import book_api.modules.database.queries as queries
import book_api.modules.database.insertions as insertions
from book_api.modules.database.db_connection import client
from pymongo.cursor import Cursor


class TestGetBookDictById(unittest.TestCase):

    def setUp(self):
        self.AddBook = insertions.AddBook("unit_test_book_title", ["unit_test_book_author"])
        self.expectedId = "f6c118034b93e80d00c4a5d116a42c00"

    def tearDown(self):
        client.drop_database("bookdb")

    def test_dict_returned_when_id_does_exist(self):
        returnedValue = queries.get_book_dict_by_id(self.expectedId)

        self.assertIsInstance(returnedValue, dict)

    def test_none_returned_when_id_does_not_exist(self):
        returnedValue = queries.get_book_dict_by_id("nonExistantDict")

        self.assertIsNone(returnedValue)


class TestGetAllBooks(unittest.TestCase):

    def setUp(self):
        insertions.AddBook("title1", ["author1"])

    def tearDown(self):
        client.drop_database("bookdb")

    def test_cursor_obj_returned(self):
        returnedValue = queries.get_all_books()

        self.assertIsInstance(returnedValue, Cursor)

    def test_all_books_found(self):
        insertions.AddBook("title2", ["author2"])

        returnedValue = queries.get_all_books()
        returnedValueLength = len(list(returnedValue))
        expectedValue = 2

        self.assertEqual(expectedValue, returnedValueLength)

    def test_full_book_dict_in_cursor(self):
        returnedValue = queries.get_all_books()
        returnedValueDict = returnedValue[0]
        expectedValue = {"authors": ["author1"],
                         "_id": "3f5468de0bfbe111586f7649a3c8d115",
                         "genres": [],
                         "isbn13": "",
                         "isbn10": "",
                         "title": "title1",
                         "tags": []}

        self.assertEqual(expectedValue, returnedValueDict)


if __name__ == "__main__":
    unittest.main()
