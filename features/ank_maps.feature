# Created by AnKrylo at 9/15/2025
Feature:ANK- Maps Page

    Background:
        Given ank I am on the dev environment login page

    @ank @regression
    Scenario: Successful login with valid credentials
        When ank I enter "akr.autotest@gmail.com" in the email field
        And ank I enter "12345" in the password field
        And ank I click the "Login " button
        When I click show on map button for device with name "Device"
        And ank I wait for 5 seconds
#        Then I should be redirected to the devices page