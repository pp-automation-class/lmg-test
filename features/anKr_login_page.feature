# Created by akryl at 9/2/2025
Feature: LinkMyGear Create an Account as a new user

    Background:
        #Given I navigate to the "Register" page
        Given anKr I navigate to "dev" environment
        And anKr I verify element page title contains text "Create an Account"

    @anKr @signup
    Scenario: Successful registration with valid email
#       When anKr I login as "user"
        When I enter "valid_email" into the "Your Email" field
        And I check "Agree to Terms and Conditions"
        Then the "Register" button should be enabled
        When I click the "Register" button
        Then I should see a confirmation message indicating that a verification email has been sent

    @anKr @invalid_email
    Scenario: Registration with invalid email
        When I enter "invalid_email" into the "Your Email" field
        And I check "Agree to Terms and Conditions"
        Then the "Register" button should remain disabled
        And I should see an error message "Please enter you email address"

    Scenario: Registration without accepting Terms and Conditions
        When I enter "user@example.com" into the "Your Email" field
        And I do not check "Agree to Terms and Conditions"
        Then the "Register" button should remain disabled
        And I should see a message prompting to accept Terms and Conditions
