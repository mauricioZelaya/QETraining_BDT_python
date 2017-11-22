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
#        | items   | GET    | 100      | Id      | 200  |
#        | items   | GET    | 10047753 | Id      | 200  |
