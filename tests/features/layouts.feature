Feature: Layout should have all links pointing to right URL
  Scenario: Visit '/home' path
    When I visit '/home' path
    Then 'home' link should have right target
    And 'help' link should have right target
    And 'about' link should have right target
    And 'contact' link should have right target
