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


class TestGetAllAuthors(unittest.TestCase):

    def setUp(self):
        insertions.AddBook("title1", ["author1"])

    def tearDown(self):
        client.drop_database("bookdb")

    def test_list_is_returned(self):
        returnedValue = queries.get_all_authors()

        self.assertIsInstance(returnedValue, list)

    def test_list_contains_strings(self):
        returnedValue = queries.get_all_authors()
        firstIndexValue = returnedValue[0]

        self.assertIsInstance(firstIndexValue, str)

    def test_item_in_lists_is_the_correct_title(self):
        returnedValue = queries.get_all_authors()
        firstIndexValue = returnedValue[0]
        expectedValue = "author1"

        self.assertEqual(expectedValue, firstIndexValue)

    def test_list_is_ecpected_length(self):
        returnedValue = queries.get_all_authors()
        returnedValueLength = len(returnedValue)
        expectedValue = 1

        self.assertEqual(expectedValue, returnedValueLength)


class TestGetBooksByAuthor(unittest.TestCase):

    def setUp(self):
        insertions.AddBook("title1", ["author1"])

    def tearDown(self):
        client.drop_database("bookdb")

    def test_cursor_obj_returned(self):
        returnedValue = queries.get_books_by_author("author1")

        self.assertIsInstance(returnedValue, Cursor)

    def test_cursor_obj_contains_dicts(self):
        returnedValue = queries.get_books_by_author("author1")
        firstIndexValue = returnedValue[0]

        self.assertIsInstance(firstIndexValue, dict)

    def test_cursor_obj_contains_expected_value(self):
        returnedValue = queries.get_books_by_author("author1")
        firstIndexValue = returnedValue[0]
        expectedValue = {"_id": "3f5468de0bfbe111586f7649a3c8d115", "title": "title1"}

        self.assertEqual(expectedValue, firstIndexValue)


class TestGetAllGenres(unittest.TestCase):

    def setUp(self):
        insertions.AddBook("title1", ["author1"], genres=["genre1", "genre2"])

    def tearDown(self):
        client.drop_database("bookdb")

    def test_list_is_returned(self):
        returnedValue = queries.get_all_genres()

        self.assertIsInstance(returnedValue, list)

    def test_list_contains_strings(self):
        returnedValue = queries.get_all_genres()
        firstIndexValue = returnedValue[0]

        self.assertIsInstance(firstIndexValue, str)

    def test_item_in_lists_is_the_correct_title(self):
        returnedValue = queries.get_all_genres()
        firstIndexValue = returnedValue[0]
        expectedValue = "genre1"

        self.assertEqual(expectedValue, firstIndexValue)

    def test_list_is_ecpected_length(self):
        returnedValue = queries.get_all_genres()
        returnedValueLength = len(returnedValue)
        expectedValue = 2

        self.assertEqual(expectedValue, returnedValueLength)


class TestGetBooksInGenre(unittest.TestCase):

    def setUp(self):
        insertions.AddBook("title1", ["author1"], genres=["genre1", "genre2"])

    def tearDown(self):
        client.drop_database("bookdb")

    def test_cursor_obj_returned(self):
        returnedValue = queries.get_books_in_genre("genre1")

        self.assertIsInstance(returnedValue, Cursor)

    def test_cursor_obj_contains_dicts(self):
        returnedValue = queries.get_books_in_genre("genre1")
        firstIndexValue = returnedValue[0]

        self.assertIsInstance(firstIndexValue, dict)

    def test_cursor_obj_contains_expected_value(self):
        returnedValue = queries.get_books_in_genre("genre1")
        firstIndexValue = returnedValue[0]
        expectedValue = {"_id": "3f5468de0bfbe111586f7649a3c8d115", "title": "title1"}

        self.assertEqual(expectedValue, firstIndexValue)


if __name__ == "__main__":
    unittest.main()
