# Created by akryl at 9/2/2025
Feature: Account Registration
    As a new user
    I want to register an account
    So that I can use the application

    Background:
        #Given I navigate to the "Register" page
        Given anKr I navigate to "https://dev.linkmygear.com/register"
        And anKr I verify element page title contains text "Create an Account"


    Scenario: Successful registration with valid email
#       When anKr I login as "user"
        When I enter "valid_email" into the "Your Email" field
        And I check "Agree to Terms and Conditions"
        Then the "Register" button should be enabled
        When I click the "Register" button
        Then I should see a confirmation message indicating that a verification email has been sent


    Scenario: Registration with invalid email
        When I enter "invalid_email" into the "Your Email" field
        And I check "Agree to Terms and Conditions"
        Then the "Register" button should remain disabled
        And I should see an error message "Please enter a valid email address"


    Scenario: Registration without accepting Terms and Conditions
        When I enter "valid_email" into the "Your Email" field
        Then I do not check "Agree to Terms and Conditions"
        And the "Register" button should remain disabled

    Scenario: Navigate to Login page from Register page
        When I click the "Log in" link
        Then I should be redirected to the "Login" page
        And I verify element page title contains text "Login to Your Account"
