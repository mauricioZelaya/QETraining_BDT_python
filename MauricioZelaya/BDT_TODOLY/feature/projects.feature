@projects
Feature: This feature is to test the implementation of the projects management feature.

  @smoke_test
  Scenario Outline: This scenario tests the basic status_code response from API projects management services.
    When I send a <method> for projects request to <service> with <format> format
    Then I should get the project status code <status_code>

    Examples:
      | method | service   | format | status_code |
      | GET    | /projects | .json  | 200         |

  @crud_test
  @acceptance_1
  #CREATE
  Scenario Outline: Confirm that a project can be added
    When I <method> the following body in <format> format to add the project with name <name>:
  """
        {
            "ProjectObject": {
              "Content": "<name>"
            }
        }
      """
    Then I get project code result <status_code>
    And the project with <name> is added.

    Examples:
      | method | name     | format | status_code |
      | POST   | project1 | .json  | 200         |
     # | none       | .json  | 400         |

  @crud_test
  @acceptance
    #MODIFY
  Scenario Outline: Confirm that a project can be updated
    When I <method> the following body in <format> format to update the project with icon: <iconId>:
  """
      {
          "ProjectObject": {
              "Content": "Project1",
              "Icon": "<iconId>"
          }
      }
      """
    Then I get project code result <status_code>
    And the project with the new icon <iconId> updated.

    Examples:
      | method | iconId | format | status_code |
      | PUT    | 5      | .json  | 200         |
     # | 9900000 | .json  | 400         |