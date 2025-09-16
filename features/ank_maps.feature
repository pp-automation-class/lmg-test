# Created by AnKrylo at 9/15/2025
Feature:ANK- Maps Page

    Background:
        Given ank I am on the dev environment login page

    @ank @regression
    Scenario: Successful login with valid credentials
        When ank I enter "akr.autotest@gmail.com" in the email field
        And ank I wait for 5 seconds
        And ank I enter "12345" in the password field
        And ank I wait for 20 seconds
        And ank I click the "Login " button
        And ank I wait for 10 seconds
        When ank I click show on map button for devices with name "name"
#        Then ank I should be redirected to the dashboard page