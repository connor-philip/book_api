from behave import given, when, then


@given("I go to the <books> endpoint")
def go_to_endpoint(context):
    pass


@then("I receive a JSON response")
@when("I receive a JSON response")
def recieve_json_response(context):
    pass


@then("the response matches the baseline")
def the_response_matches_the_baseline(context):
    pass
