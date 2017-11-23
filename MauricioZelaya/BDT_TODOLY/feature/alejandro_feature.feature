@alejandro
Feature: This feature will evaluate CURD for item for the services create, get and update items

  @smoke_test
  Scenario Outline: I'm performing a regression test for item service for the method create get and update
    Given I get a <service>
    When I also get a <method> to validate
    And I get an <itemId> to search
    Then I get the <code> response to validate

    Examples:
      | service | method | itemId   | code |
      | items   | GET    | 10047753 | 200  |


  @acceptance_test
  Scenario Outline: I want to verify that I get the items associated to my account
    Given I get a <service>
    When I also get a <method> to validate
    And I get an <itemId> to search
    Then I get the <code> response to validate
    And I verify the <itemKey> in the response


    Examples:
      | service | method | itemId   | itemKey | code |
      | items   | GET    | 10047753 | Id      | 200  |
      | items   | GET    | 100      | Id      | 400  |
      | items   | GET    | 10047753 | Id      | 200  |

  @acceptance_test_put
  Scenario Outline: given an item I want to verify that an item can be edited and verify the new parameters are correct
    Given I get an <itemId> to modify
    And I get a <service>
    And I get a <parameter> to modify
    And I also get a <value> to modify
    When I make the <method> request
    Then I get the <code> response to validate
    And I verify that the parameter has change in the response

    Examples:
      | itemId   | method | parameter | value | code | service |
      | 10047753 | PUT    | Priority  | 1     | 200  | items   |

