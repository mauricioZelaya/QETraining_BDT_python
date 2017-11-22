@projects
Feature: This feature is to test the implementation of the projects management feature.

  @smoke_test
  Scenario Outline: This scenario tests the basic status_code response from API projects management services.
    When I send a <method> request to <service> with <format> format
    Then I get status code <status_code>

    Examples:
      | method | service     | format | status_code |
      | GET    | /projects   | .json  | 200         |
      | DELETE | /projects/0 | .json  | 400         |

  @crud_test
  @acceptance
  Scenario Outline: Confirm that a project can be updated
    When I post the following body in <format> format to update the project with ID <ID>:
  """
      {
          "ProjectObject": {
              "Content": "ProjectNameModified1",
              "Icon": "4"
          }
      }
      """
    Then I get status code <status_code>
    And the edited project with the new data.

    Examples:
      | ID      | format | status_code |
      | 3354231 | .json  | 200         |
      | 9900000 | .json  | 400         |