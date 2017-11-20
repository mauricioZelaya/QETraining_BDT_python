@captions
Feature: This will test the search method feature for the API in youtube

  @smoke_test
  Scenario Outline: I would like to make a regression and obtain the response on the search service
    When I need to test the response in the <service> using <method>
    And Looking for <video> id
    Then I get response with <code> code

    Examples:
      | service   | method | code | video       |
      | /captions | GET    | 200  | M7FIvfx5J10 |


  @acceptance_test
  Scenario Outline: I want to perform search of a determined video with caption using several inputs and
  I have to validate the response .json
    When I need to test the response in the <service> using <method>
    And Looking for <video> id
    Then I get response with <code> code
    And A <key> of response equals to <kind>

    Examples:
      | service   | method | code | kind                        | key  | video       |
      | /captions | GET    | 200  | youtube#captionListResponse | kind | M7FIvfx5J10 |
