@playlist
  Feature: playlist_feature
    @smoke
    Scenario: smoke test for getting a playlist
      Given an authenticated user
      When I send a GET playlist
      Then I get a status code 200
