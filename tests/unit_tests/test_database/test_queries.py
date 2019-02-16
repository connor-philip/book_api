import unittest
import book_api.modules.database.queries as queries
import book_api.modules.database.insertions as insertions
from book_api.modules.database.db_connection import client


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


if __name__ == "__main__":
    unittest.main()
