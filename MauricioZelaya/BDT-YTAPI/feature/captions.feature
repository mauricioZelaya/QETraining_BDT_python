@captions
Feature: This will test the search method feature for the API in youtube

  @smoke_test
  Scenario Outline: I would like to make a regression and obtain the response on the search service
    When I need to test the response in the <service> method with <snippet> using <method>
    And Looking for <video> id
    Then I get response with <code> code

    Examples:
      | service   | method | code | video       | snippet |
      | /captions | GET    | 200  | M7FIvfx5J10 | snippet |

