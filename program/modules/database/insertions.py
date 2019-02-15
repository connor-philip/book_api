

class AddBook:

    def __init__(self):
        pass

    def format_type_error_message(self, description, expectedType, incorrectValue):
        actualType = type(incorrectValue)
        errorMessage = "\n{} is not a {}:\n\t{}\nInstead type is: {}".format(description,
                                                                             expectedType,
                                                                             incorrectValue,
                                                                             actualType)
        return errorMessage

    def unexpected_length_error_message(self, description, expectedLength, incorrectValue):
        errorMessage = "{} does not have the expected length of {}\nGot: {}".format(description,
                                                                                    expectedLength,
                                                                                    incorrectValue)
        return errorMessage

    def check_if_book_dict_has_valid_values(self, title, authors, genres=[], tags=[], isbn10="", isbn13=""):
        errorMessage = ""

        # Check parameter types
        for strParam in [title, isbn10, isbn13]:
            if isinstance(strParam, str) is False:
                errorMessageLine = self.format_type_error_message(strParam, "str", strParam)
                errorMessage = "{}\n{}".format(errorMessage, errorMessageLine)

        for listParam in [genres, authors, tags]:
            if isinstance(listParam, list):
                for strItem in listParam:
                    if isinstance(strItem, str) is False:
                        description = "{} list item".format(listParam)
                        errorMessageLine = self.format_type_error_message(description, "str", strItem)
                        errorMessage = "{}\n{}".format(errorMessage, errorMessageLine)
            else:
                errorMessageLine = self.format_type_error_message(listParam, "list", listParam)
                errorMessage = "{}\n{}".format(errorMessage, errorMessageLine)

        # Ensure ISBN have correct length
        if isbn10 and len(isbn10) != 10:
            errorMessageLine = self.unexpected_length_error_message("ISBN-10", "10", isbn10)
            errorMessage = "{}\n{}".format(errorMessage, errorMessageLine)
        if isbn13 and len(isbn13) != 13:
            errorMessageLine = self.unexpected_length_error_message("ISBN-13", "13", isbn13)
            errorMessage = "{}\n{}".format(errorMessage, errorMessageLine)

        # If error message is empty return True
        if errorMessage:
            print(errorMessage)
            return False
        else:
            return True

    def create_new_book_dict_with_selected_keys(self, newBookDict):
        pass

    def create_and_append_book_id(self, newBookDict):
        # md5(title + isbn-10 + isbn-13)
        pass

    def add_book_to_db(self, bookDict):
        pass
