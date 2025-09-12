Feature: LS Login Page
  As a user
  I want quick access to account recovery and creation
  So that I can reset my password or create a new account

  Background:
    Given I am on the dev environment login page

  @ls @login
  Scenario: Successful user login with valid credentials
    When ls I enter "lauravstesting53@gmail.com" in the email field
    And ls I enter "T8st8ng38!" in the password field
    And ls I click the login button
    Then ls I should be redirected to the devices page


  @ls @login
  Scenario: Sign up link navigates to registration page
    When I click the "Sign Up" link
    Then I should be redirected to the registration page
    And I should see "Create your account" heading
