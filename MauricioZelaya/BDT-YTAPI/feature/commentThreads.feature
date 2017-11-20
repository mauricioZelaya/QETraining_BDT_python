@commentThreads
  Feature: comment_Threads_feature
    @smoke
    Scenario: smoke test for get comment threads for a given video ID
      Given 2G5rfPISIwo video id for a comment thread
      When I send a GET comment threads list using /commentThreads
      Then status code 200 is received

#    Scenario: smoke test to insert a new comment thread
#      Given  { "snippet": {  "videoId": "GfFKTrH98Lg",  "topLevelComment": {   "snippet": {    "textOriginal": "new api comment test"   }  },  "channelId": "UCuWIzsqTAHomWXl5qnWZBJA" }} body
#      When I POST the comment using /commentThreads service
#      Then get 200
