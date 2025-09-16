Feature: TaPi Login Page
  As a user
  I want to be able to log into the application
  So that I can access my account and protected features

  Background:
    Given I am on the dev environment login page

  @positive @login
  Scenario: Successful login with valid credentials
    When I enter "testanya108+amn@gmail.com" in the email field
    And I enter "54321" in the password field
    And I click the login button
    Then TaPi should be redirected to the devices page

  @negative @login
  Scenario: Failed login with invalid password
    When I enter "testanya108+amn@gmail.com" in the email field
    And I enter "99999" in the password field
    And I click the login button
    Then TaPi should remain on the login page
    And TaPi should see error message "Sorry, unrecognized username or password"

  @negative @login
  Scenario: Failed login with invalid email
    When I enter "not-an-email" in the email field
    And I enter "54321" in the password field
    And I click the login button
    Then TaPi should remain on the login page
    And TaPi should see error message "Sorry, unrecognized username or password"
