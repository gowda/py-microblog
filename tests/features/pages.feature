Feature: Respond to '/home', '/help' paths
  Scenario: Visit '/home' path
    When I visit '/home' path
    Then I should get a '200' response
    And title set to 'py-microblog - home'
  Scenario: Visit '/help' path
    When I visit '/help' path
    Then I should get a '200' response
    And title set to 'py-microblog - help'
  Scenario: Visit '/about' path
    When I visit '/about' path
    Then I should get a '200' response
    And title set to 'py-microblog - about'
  Scenario: Visit '/contact' path
    When I visit '/contact' path
    Then I should get a '200' response
    And title set to 'py-microblog - contact'
