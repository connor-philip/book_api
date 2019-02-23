import unittest
import book_api.modules.ba_logging.message_formatters as message_formatters


class TestFormatTypeErrorMessage(unittest.TestCase):

    def test_(self):
        pass

    def test_string_is_returned(self):
        returnedValue = message_formatters.format_type_error_message("description",
                                                                     "expectedType",
                                                                     "incorrectValue")

        self.assertIsInstance(returnedValue, str)

    def test_string_is_formatted_as_expected(self):
        returnedValue = message_formatters.format_type_error_message("description",
                                                                     "expectedType",
                                                                     "incorrectValue")
        expectedValue = "\ndescription is not a expectedType:\n\tincorrectValue\nInstead type is: <class 'str'>"

        self.assertEqual(expectedValue, returnedValue)


class TestUnexpectedLengthErrorMessage(unittest.TestCase):

    def test_string_is_returned(self):
        returnedValue = message_formatters.unexpected_length_error_message("description",
                                                                           "expectedLength",
                                                                           "incorrectValue")

        self.assertIsInstance(returnedValue, str)

    def test_string_is_formatted_as_expected(self):
        returnedValue = message_formatters.unexpected_length_error_message("description",
                                                                           "expectedLength",
                                                                           "incorrectValue")
        expectedValue = "description does not have the expected length of expectedLength\nGot: incorrectValue"

        self.assertEqual(expectedValue, returnedValue)


if __name__ == "__main__":
    unittest.main()
