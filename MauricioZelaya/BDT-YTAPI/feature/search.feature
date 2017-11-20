@search
Feature: This will test the search method feature for the API in youtube

  @smoke_test
  Scenario Outline: I would like to make a regression and obtain the response on the search service
    When I need to test the response in the <service> using <method>
    Then I get response with <code> code

    Examples:
      | service | method | code |
      | /search | GET    | 200  |

  @acceptance_test
  Scenario Outline: I want to perform search using several inputs and validate the response .json
    When I need to test the response in the <service> using <method>
    And I have to use a <keyword> to search
    Then I get response with <code> code
    And A <key> of response equals to <kind>

    Examples:
      | service | method | code | kind                       | keyword | key        |
      | /search | GET    | 200  | youtube#searchListResponse | Nirvana | kind       |
      | /search | GET    | 200  | BO                         | Nirvana | regionCode |
