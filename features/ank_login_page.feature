# Created by akryl at 9/2/2025
Feature:ANK- Login Page
  As a user
  I want to be able to log into the application
  So that I can access my account and protected features

    Background:
        Given ank I am on the dev environment login page

    @regression @login @positive
    Scenario: Successful login with valid credentials
        When ank I enter "akr.autotest@gmail.com" in the email field
        And ank I enter "12345" in the password field
        And ank I click the login button
#        And Wait for 5 seconds
#        Then ank I should be redirected to the devices page

    @negative @login
    Scenario: Failed login with invalid password
        When ank I enter invalid email in the email field
        And ank I enter "InvalidPassword!" in the password field
        And ank I click the login button
#        Then ank I should remain on the login page
#        And ank I should see error message "Invalid email or password"

    @negative @login
    Scenario: Failed login with invalid email
        When ank I enter "autotest@gmail.com" in the email field
        And ank I enter "12345" in the password field
        And ank I click the login button
#        Then ank I should remain on the login page
#        And ank I should see error message "Please enter a valid email address"

      @negative @login
#    Scenario: Failed login with empty credentials
#        When I click the login button
#        Then I should remain on the login page
#        And I should see error message "Email is required"
#        And I should see error message "Password is required"

