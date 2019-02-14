

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

    def check_if_book_dict_has_valid_values(self, title, genres, authors=[], tags=[], isbn10="", isbn13=""):
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

        # If error message is empty return True
        if errorMessage:
            print(errorMessage)
            return False
        else:
            return True

    def create_new_book_dict_with_selected_keys(self, newBookDict):
        pass

    def create_and_append_book_id(self, newBookDict):
        pass

    def add_book_to_db(self, bookDict):
        pass
