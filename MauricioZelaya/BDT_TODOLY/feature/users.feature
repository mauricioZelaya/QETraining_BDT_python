@users
Feature:

  @smoke_test
  Scenario Outline: smoke testing for methods of user and authentication services
    When I send a <method> request to <service>
    Then I get status code <status_code>

    Examples:
      | method | service                        | status_code |
      | GET    | user                           | 200         |
      | GET    | authentication/isauthenticated | 200         |
      | GET    | authentication/token           | 200         |
      | POST   | user                           | 400         |
      | PUT    | user/0                         | 400         |
#      | DELETE | user/0                         | 200         |


  @crud_test
  Scenario: getting profile information of an authenticated user
    Given an authenticated user zelaya.mauricio@gmail.com and Mauricio Zelaya
    When I GET the user service method to request user information
    Then I receive status code 200
    And I compare result to validate the mail and fullname are aslo received


  @crud_test
  Scenario: updating user information
    Given an authenticated user with zelaya.mauricio@gmail.com email
    When I PUT request to change the full name to other Zelaya using user/0 service
    Then I get response code 200
      And The new name is part of the response
