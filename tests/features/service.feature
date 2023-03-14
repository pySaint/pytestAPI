Feature: DuckDuckGo Instant Answer API
  As an application developer,
  I want to get instant answers for search terms via a REST API,
  So that my app can get answers anywhere.


  Scenario: Basic DuckDuckGo API Query
    Given the DuckDuckGo API is queried with "panda"
    Then the response status code is "200"
    And the response contains results for "panda"

