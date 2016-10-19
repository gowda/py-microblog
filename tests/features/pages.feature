Feature: Respond to '/home', '/help' paths
  Scenario: Visit '/home' path
    When I visit '/home' path
    Then I should get a '200' response
  Scenario: Visit '/help' path
    When I visit '/help' path
    Then I should get a '200' response
