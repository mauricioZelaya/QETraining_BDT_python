@crud
Feature: This will test the Items method feature for the API in todo
  Scenario Outline: I want to perform list of the items
    When I send the <service> and using the <method>
    Then I get response with <code> code

    Examples:
      | service     | method | code |
      | /items.json | GET    | 200  |