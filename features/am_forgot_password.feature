Feature: am: Forgot Password
  As a user who forgot their password
  I want to reset my password
  So that I can regain access to my account

  Background:
    Given am: I navigate to the dev environment login page
    When  am: I click on "Forgot password" link
    Then  am: I wait for "Restore Password" form to be visible

  @am-smoke @am-forgot_password @am-positive
  Scenario: am: Successful request with valid email
    When am: I fill valid email in the restore email field
    And  am: I click on "Send" button
    Then am: I get the strange message. Let's assume that everything is fine :)

  @am-negative @am-forgot_password
  Scenario: am: Failed request with empty email
    When am: I don't fill the restore email field
    And  am: I click on email label to trigger validation
    Then am: I get "The empty restore email" error message

  @am-negative @am-forgot_password
  Scenario: am: Failed request with wrong format email
    When am: I fill "Wrong.format" in the restore email field
    And  am: I click on email label to trigger validation
    Then am: I get "The wrong format restore email" error message