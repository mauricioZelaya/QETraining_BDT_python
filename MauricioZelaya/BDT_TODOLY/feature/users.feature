@users
Feature:

  @smoke_test
  Scenario Outline:
    When I send a <method> request to <service> with <format> format
    Then I get status code <status_code>

    Examples:
      | method | service                         | format | status_code |
      | GET    | /user                           | .json  | 200         |
      | GET    | /authentication/isauthenticated | .json  | 200         |
      | GET    | /authentication/token           | .json  | 200         |
      | DELETE | /user/0                         | .json  | 200         |


