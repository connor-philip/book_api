@api
@status_codes

Feature: Test the status codes for the API endpoints.


Scenario Outline: I recieve the expected status codes
    Given I go to the <Endpoint> endpoint
    Then I recieve the status code <StatusCode>
    Examples: Full endpoint addresses
    | Endpoint                                      | StatusCode |
    | "api/books/"                                  | "200"      |
    | "api/books/3ce55a9fb44a345f712b1360c2bf9d29"  | "200"      |
    | "api/authors/"                                | "200"      |
    | "api/authors/Albert Camus"                    | "200"      |
    | "api/genres/"                                 | "200"      |
    | "api/genres/fiction"                          | "200"      |

    Examples: 308 Redirects
    | Endpoint                                     | StatusCode |
    | "api/books"                                  | "308"      |
    | "api/authors"                                | "308"      |
    | "api/genres"                                 | "308"      |
