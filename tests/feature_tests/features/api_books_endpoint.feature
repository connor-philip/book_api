Feature: Test the books endpoint of the book_api

Scenario: api/books endpoint returns JSON
    Given I go to the "api/books" endpoint
    Then I receive a JSON response


Scenario Outline: These endpoints give the expected data
    Given I go to the <Endpoint> endpoint
    When I receive a JSON response
    Then the response matches the baseline file <Baseline>

    Examples:
    | Endpoint                                      | Baseline              |
    | "api/books"                                   | "books.json"          |
    | "api/books/3ce55a9fb44a345f712b1360c2bf9d29"  | "books_book.json"     |
    | "api/authors"                                 | "authors.json"        |
    | "api/authors/Albert Camus"                    | "authors_author.json" |
    | "api/genres"                                  | "genres.json"         |
    | "api/genres/fiction"                          | "genres_genre.json"   |