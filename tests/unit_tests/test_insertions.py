import unittest
import insertions


class TestCheckIfBookDictHasValidValues(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_true_returned_on_success(self):
        pass

    def test_false_returned_on_error(self):
        pass

    def test_title_must_be_string(self):
        pass

    def test_genres_must_be_list(self):
        pass

    def test_genres_list_must_contain_strings(self):
        pass

    def test_authors_must_be_list(self):
        pass

    def test_authors_list_must_contain_strings(self):
        pass

    def test_tags_must_be_list(self):
        pass

    def test_tags_list_must_contain_strings(self):
        pass

    def test_isbn_10_must_be_string(self):
        pass

    def test_isbn_10_must_have_length_of_10(self):
        pass

    def test_isbn_13_must_be_string(self):
        pass

    def test_isbn_13_must_have_length_of_13(self):
        pass


class TestCreateNewBookDictWithSelectedKeys(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_dict_is_returned(self):
        pass

    def test_extra_keys_are_not_included(self):
        pass


class TestCreateAndAppendBookId(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_id_is_appened_to_book_dict(self):
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
