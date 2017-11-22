@items
Feature: This will test the Items method feature for the API in todo

  Scenario Outline: I want to perform list of the items
    When I send the <SERVICE> with the <FORMAT>
    And I used the <METHOD>
    Then I get the response with <CODE> code

    Examples:
      | SERVICE | FORMAT | METHOD | CODE |
      | /items  | .json  | GET    | 200  |