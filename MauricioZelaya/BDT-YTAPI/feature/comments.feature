@comments
  Feature: comments_feature
    @smoke
    Scenario: smoke test for get comments
      Given z13icrq45mzjfvkpv04ce54gbnjgvroojf0 parent id for a comment
      When I send a GET comments list using /comments
      Then I get a status code 200

#    Scenario: smoke test to add a new comment reply
#      Given