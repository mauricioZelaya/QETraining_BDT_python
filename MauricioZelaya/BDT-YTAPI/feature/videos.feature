@videos
Feature: This will test the video method feature for the API in youtube

  @smoke_test
  Scenario Outline: I would like to make a regression and obtain the response on the video service
    When Test the response in the <service> using <method>
      And selection the <video> id
    Then The response with <code> code

    Examples:
      | service   | method | code | video       |
      | /videos   | GET    | 200  | Ks-_Mh1QhMc |
