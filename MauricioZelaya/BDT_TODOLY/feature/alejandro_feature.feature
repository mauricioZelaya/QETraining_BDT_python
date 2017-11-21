Feature: This feature will evaluate CURD for item for the services create, get and update items

  @smoke_test
  Scenario: I'm performing a regression test for item service for the method create get and update
    When I get a service <method> to validate
    Then I get the <code> response to validate




