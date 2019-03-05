Feature: Test the books endpoint of the book_api

Scenario: /api/books endpoint returns JSON
    Given I go to the <books> endpoint
    Then I receive a JSON response


Scenario: /api/books JSON contains all of the books in the api
    Given I go to the <books> endpoint
    When I receive a JSON response
    Then the response matches the baseline