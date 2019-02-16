import unittest
import book_api.modules.database.insertions as insertions


class TestCheckIfBookDictHasValidValues(unittest.TestCase):

    def setUp(self):
        self.AddBook = insertions.AddBook()

    def test_true_returned_on_success(self):
        result = self.AddBook.check_if_book_dict_has_valid_values("Book-Title",
                                                                  ["author"])

        self.assertTrue(result)

    def test_false_returned_on_error(self):
        result = self.AddBook.check_if_book_dict_has_valid_values("Book-Title",
                                                                  ["author", False])

        self.assertFalse(result)

    def test_title_must_be_string(self):
        result = self.AddBook.check_if_book_dict_has_valid_values(False, ["author"])

        self.assertFalse(result)

    def test_genres_must_be_list(self):
        result = self.AddBook.check_if_book_dict_has_valid_values("Book-Title",
                                                                  ["author"],
                                                                  genres=False)

        self.assertFalse(result)

    def test_genres_list_must_contain_strings(self):
        result = self.AddBook.check_if_book_dict_has_valid_values("Book-Title",
                                                                  ["author"],
                                                                  genres=[False])

        self.assertFalse(result)

    def test_authors_must_be_list(self):
        result = self.AddBook.check_if_book_dict_has_valid_values("Book-Title",
                                                                  False)

        self.assertFalse(result)

    def test_authors_list_must_contain_strings(self):
        result = self.AddBook.check_if_book_dict_has_valid_values("Book-Title",
                                                                  [False])

        self.assertFalse(result)

    def test_tags_must_be_list(self):
        result = self.AddBook.check_if_book_dict_has_valid_values("Book-Title",
                                                                  ["author"],
                                                                  tags=False)

        self.assertFalse(result)

    def test_tags_list_must_contain_strings(self):
        result = self.AddBook.check_if_book_dict_has_valid_values("Book-Title",
                                                                  ["author"],
                                                                  tags=[False])

        self.assertFalse(result)

    def test_isbn_10_must_be_string(self):
        result = self.AddBook.check_if_book_dict_has_valid_values("Book-Title",
                                                                  ["author"],
                                                                  isbn10=False)

        self.assertFalse(result)

    def test_isbn_10_must_have_length_of_10(self):
        result = self.AddBook.check_if_book_dict_has_valid_values("Book-Title",
                                                                  ["author"],
                                                                  isbn10="12345678911")

        self.assertFalse(result)

    def test_isbn_13_must_be_string(self):
        result = self.AddBook.check_if_book_dict_has_valid_values("Book-Title",
                                                                  ["author"],
                                                                  isbn13=False)

        self.assertFalse(result)

    def test_isbn_13_must_have_length_of_13(self):
        result = self.AddBook.check_if_book_dict_has_valid_values("Book-Title",
                                                                  ["author"],
                                                                  isbn13="12345678912345")

        self.assertFalse(result)

    def test_title_is_required(self):
        self.assertRaises(TypeError, self.AddBook.check_if_book_dict_has_valid_values)

    def test_authors_is_required(self):
        self.assertRaises(TypeError, self.AddBook.check_if_book_dict_has_valid_values, "title")


class TestCreateBookId(unittest.TestCase):

    def setUp(self):
        self.AddBook = insertions.AddBook()

    def test_string_is_returned(self):
        returnedValue = self.AddBook.create_book_id("title", "isbn-10", "isbn-13")

        self.assertIsInstance(returnedValue, str)

    def test_id_is_predictable(self):
        returnedValue = self.AddBook.create_book_id("title", "isbn-10", "isbn-13")
        expectedValue = "8abf045d105db432e476ebfce5f7ffba"

        self.assertEqual(returnedValue, expectedValue)

    def test_isbn10_is_optional(self):
        returnedValue = self.AddBook.create_book_id("title", "isbn-13")
        expectedValue = "e8290b7ad427338ab3c6e60f99792a23"

        self.assertEqual(returnedValue, expectedValue)

    def test_isbn13_is_optional(self):
        returnedValue = self.AddBook.create_book_id("title", "isbn-10")
        expectedValue = "a40823e593399c9ca260561118e39cba"

        self.assertEqual(returnedValue, expectedValue)

    def test_title_is_required(self):
        self.assertRaises(TypeError, self.AddBook.create_book_id)


class TestCreateBookDict(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_dict_is_returned(self):
        pass

    def test_extra_keys_are_not_included(self):
        pass


class TestAddBookToDb(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_true_returned_on_success(self):
        pass

    def test_false_returned_on_error(self):
        pass

    def test_book_added_to_db(self):
        pass


if __name__ == "__main__":
    unittest.main()