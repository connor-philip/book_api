
def format_type_error_message(description, expectedType, incorrectValue):
    actualType = type(incorrectValue)
    errorMessage = "\n{} is not a {}:\n\t{}\nInstead type is: {}".format(description,
                                                                         expectedType,
                                                                         incorrectValue,
                                                                         actualType)
    return errorMessage


def unexpected_length_error_message(description, expectedLength, incorrectValue):
    errorMessage = "{} does not have the expected length of {}\nGot: {}".format(description,
                                                                                expectedLength,
                                                                                incorrectValue)
    return errorMessage
