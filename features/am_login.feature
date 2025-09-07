Feature: Login
  As a registered user
  I want to log into the application
  So I can access my account and fratures

  Background:
    Given am: I navigate to the dev environment login page

  @smoke @login
  Scenario: am: Successful login with valid credentials
    Given am: I enter valid email in the email field
    And   am: I enter valid password in the password field
    When  am: I click the login button
    Then  am: I should be redirected to the devices page

  @negative @login
  Scenario: Failed login with invalid password
    Given am: I enter "test@example.com" in the email field
    And   am: I enter "ValidPass123!" in the password field
    When  am: I click the login button
    Then am: I get the invalod login error message


  Scenario: Failed login with invalid email and valid password
  Scenario: Failed login with invalid credentials
  Scenario: Failed login with valid email and invalid password
  Scenario: Failed login with empty email
  Scenario: Failed login with wrong format email
