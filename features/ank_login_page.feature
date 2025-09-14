# Created by akryl at 9/2/2025
Feature:ANK- Login Page
  As a user
  I want to be able to log into the application
  So that I can access my account and protected features

    Background:
        Given ank I am on the dev environment login page

    @positive @login
    Scenario: "Create an account" link navigates to registration page
        When ank I click the "Create an Account" link
        Then ank I should be redirected to registration page
        And ank I should see "Create an Account" heading

    @regression @login @positive
    Scenario: Successful login with valid credentials
        When ank I enter "akr.autotest@gmail.com" in the email field
        And ank I enter "12345" in the password field
        And ank I click the "Login " button
#        And ank Wait for 5 seconds
        Then ank I should be redirected to the dashboard page

    @negative @login
    Scenario: Failed login with invalid email
        When ank I enter "autotest@gmail.com" in the email field
        And ank I enter "12345" in the password field
        And ank I click the "Login " button
        And ank I should see error message "Sorry, unrecognized username or password"

      @negative @login
    Scenario: Failed login with empty credentials
        When ank I click the "Login " button
        And ank I should see error message "Email is required"
        And ank I should see error message "Password is required"
#
    @negative @login
    Scenario: Forgot password link navigates to reset page
        When ank I click on forgot the password link
        Then ank I should be redirected to password restore page
        And ank I should see "Restore Password" heading
        And ank I enter "akr.autotest@gmail.com" in the email field
        And ank I click the "Send" button
