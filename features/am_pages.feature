Feature: am: Swith Pages tests

  Background:
    Given am: I navigate to the dev-v2 environment login page
    When  am: I login with valid credentials
    Then  am: I should be redirected to the devices page

  Scenario: am: Show Device on Map
    Given am: I click on button "Show on map" for device "John1"
    Then  am: I should be redirected to the new Google Maps page
    When  am: I click button "Directions" on Google Maps page
    And   am: I click button "Driving" on Google Maps page
    And   am: I input "713 Brighton Beach Ave, Brooklyn, NY 11235" in the starting point field
    And   am: I press Enter key
    And   am: I wait for 20 seconds
    Then  am: I close the Google Maps page and return to the devices page
    And   am: I should be redirected to the devices page