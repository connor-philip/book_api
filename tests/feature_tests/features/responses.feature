@api

Feature: Test the endpoints give the expected response


Scenario Outline: These endpoints serve json
    Given I go to the <Endpoint> endpoint
    Then I receive a JSON response
    Examples:
    | Endpoint                                      |
    | "api/books/"                                  |
    | "api/books/3ce55a9fb44a345f712b1360c2bf9d29"  |
    | "api/authors/"                                |
    | "api/authors/Albert Camus"                    |
    | "api/genres/"                                 |
    | "api/genres/fiction"                          |


@baseline
Scenario Outline: These GET endpoints give the expected data
    Given I go to the <Endpoint> endpoint
    When I receive a JSON response
    Then the response matches the baseline file <Baseline>
    Examples: Successful GET responses
    | Endpoint                                      | Baseline              |
    | "api/books/"                                  | "books.json"          |
    | "api/books/3ce55a9fb44a345f712b1360c2bf9d29"  | "books_book.json"     |
    | "api/authors/"                                | "authors.json"        |
    | "api/authors/Albert Camus"                    | "authors_author.json" |
    | "api/genres/"                                 | "genres.json"         |
    | "api/genres/fiction"                          | "genres_genre.json"   |

    # Examples: Unsuccessful GET responses
    # | Endpoint                                      | Baseline              |
    # | "api/books/invalid_id"                        | "books_book.json"     |
    # | "api/authors/Ghost Writer"                    | "authors_author.json" |
    # | "api/genres/Ficticous non-fiction"            | "genres_genre.json"   |


@baseline
Scenario Outline: These POST endpoints give the expected data
    Given I "POST" the data <PostData> to the <Endpoint> endpoint
    When I receive a JSON response
    Then the response matches the baseline file <Baseline>
    Examples: Successful POST responses
    | Endpoint              | PostData                    | Baseline                  |
    | "api/books/add_book"  | "crime_and_punishment.json" | "add_book_success.json"   |

    Examples: Unsuccessful POST responses
    | Endpoint              | PostData                    | Baseline                  |
    | "api/books/add_book"  | "invalid_book_object.json"  | "add_book_error.json"     |