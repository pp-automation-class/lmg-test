Feature: am: Login
  As a registered user
  I want to log into the application
  So I can access my account and fratures

  Background:
    Given am: I navigate to the dev environment login page

  @smoke @login @positive
  Scenario: am: Successful login with valid credentials
    Given am: I enter valid email in the email field
    And   am: I enter valid password in the password field
    When  am: I click the login button
    Then  am: I should be redirected to the devices page

  @negative @login
  Scenario: Failed login with invalid password
    Given am: I enter valid email in the email field
    And   am: I enter "InvalidPass123!" in the password field
    When  am: I click the login button
    Then  am: I get the invalid login error message

  @negative @login
  Scenario: Failed login with invalid email and valid password
    Given am: I enter "invalid@example.com" in the email field
    And   am: I enter valid password in the password field
    When  am: I click the login button
    Then  am: I get the invalid login error message

  @negative @login
  Scenario: Failed login with invalid credentials
    Given am: I enter "invalid@example.com" in the email field
    And   am: I enter "InvalidPass123!" in the password field
    When  am: I click the login button
    Then  am: I get the invalid login error message

  @negative @login
  Scenario: Failed login with empty email
    Given am: I don't fill the email field
    And   am: I enter valid password in the password field
    When  am: I click the login button
    Then  am: I get the empty email error message

  @negative @login
  Scenario: Failed login with empty password
    Given am: I enter valid email in the email field
    And   am: I don't fill the password field
    When  am: I click the login button
    Then  am: I get the empty password error message

