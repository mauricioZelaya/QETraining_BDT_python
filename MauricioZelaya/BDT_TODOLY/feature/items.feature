@items
Feature: This will test the Items method feature for the API in todo

  @smoke_test
  Scenario Outline: I want to perform list of the items
    When I send the <SERVICE>
    And I used the <METHOD>
    Then I get the response with <CODE> code

    Examples:
      | SERVICE | METHOD | CODE |
      | items   | GET    | 200  |


  Scenario Outline: I want to perform delete of a item
    Given A <SERVICE> and a <METHOD>
    When I select a <ID> of the item
    Then I get the result equals to <CODE>

    Examples:
      | SERVICE | METHOD | ID   | CODE |
      | items   | DELETE | 1033 | 200  |