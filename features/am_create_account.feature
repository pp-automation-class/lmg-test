Feature: am: Create Account
  As a new visitor
  I want to create an account
  So I can log in and use application features

  Background:
    Given am: I navigate to the dev environment login page
    When  am: I click on "Create an account" link
    Then  am: I wait for "Create an Account" form to be visible

  @am-smoke @am-registration @am-positive
  Scenario: am: Successful User registration with a new valid email
    When am: I fill a random email in email input field
    And  am: I check the terms and conditions checkbox
    And  am: I click on "Register" button
    Then  am: I should be redirected to the devices page

  @am-negative @am-registration
  Scenario: am: Failed User registration with existing email
    When am: I fill an existed email in email input field
    And  am: I check the terms and conditions checkbox
    And  am: I click on "Register" button
    Then am: I get "The user already exists" error message

  @am-negative @am-registration
  Scenario: am: Failed User registration with empty email
    When am: I click on registration email label to trigger validation
    And  am: I check the terms and conditions checkbox
    Then am: I get "Please enter you email address" error message

  @am-negative @am-registration
  Scenario: am: Failed User registration with wrong format email
    When am: I fill "Wrong.email" in email input field
    And  am: I check the terms and conditions checkbox
    Then am: I get "Please enter a valid email address" error message
