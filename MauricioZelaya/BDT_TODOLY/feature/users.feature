@users
Feature:

  @smoke_test
  Scenario Outline: smoke testing for methods of user and authentication services
    When I send a <method> request to <service> with <format> format
    Then I get status code <status_code>

    Examples:
      | method | service                         | format | status_code |
      | GET    | /user                           | .json  | 200         |
      | GET    | /authentication/isauthenticated | .json  | 200         |
      | GET    | /authentication/token           | .json  | 200         |
#      | DELETE | /user/0                         | .json  | 200         |

  @crud_test
  Scenario:
    Given .json format for the response
  When I GET the /user service method to request user information
  Then I receive status code 200
    And I compare result
  """
    {
    "Id": 590111,
    "Email": "zelaya.mauricio@gmail.com",
    "Password": null,
    "FullName": "bdtgroup",
    "TimeZone": 0,
    "IsProUser": false,
    "DefaultProjectId": 3662638,
    "AddItemMoreExpanded": false,
    "EditDueDateMoreExpanded": false,
    "ListSortType": 0,
    "FirstDayOfWeek": 0,
    "NewTaskDueDate": -1,
    "TimeZoneId": "Pacific Standard Time"
  }
  """

