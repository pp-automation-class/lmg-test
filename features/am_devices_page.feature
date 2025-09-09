Feature: am: Devices Page tests
  Log in and verify elements on the devices page
  I now have access to my devices and their details
  So I can manage and monitor them effectively

  Background:
    Given am: I navigate to the dev environment login page
    When  am: I login with valid credentials
    Then  am: I should be redirected to the devices page

  Scenario: am: Verify Devices Page Elements
    Then  am: I Check List of devices