@projects
Feature: This feature is to test the implementation of the projects management feature.

  @smoke_test
  Scenario Outline: This scenario tests the basic status_code response from API projects management services.
    When I send a <method> for projects request to <service> with <format> format
    Then Getting status code project operation <status_code>

    Examples:
      | method | service   | format | status_code |
      | GET    | /projects | .json  | 200         |
     # | DELETE | /projects/0 | .json  | 400         |


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
    And the new project is added.

    Examples:
      | method | name     | format | status_code |
      | POST   | project1 | .json  | 200         |
     # | none       | .json  | 400         |