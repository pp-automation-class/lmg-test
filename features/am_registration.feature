Feature: User Registration on UltimateQA Courses
  As a new visitor
  I want to create a new account
  So that I can access the courses portal

  Background:
    Given I am on the UltimateQA sign in page

  @registration @smoke
  Scenario: Successful new user registration
    When I navigate to the registration page
    And I register a new user with a unique email
    Then I should see a confirmation or onboarding page

  @registration @negative
  Scenario: Attempt registration with an already used email
    When I navigate to the registration page
    And I fill registration form with email "already-used@example.com" first name "John" last name "Tester" password "ValidPass123!"
    And I submit the registration form
    Then I should see a registration error message
