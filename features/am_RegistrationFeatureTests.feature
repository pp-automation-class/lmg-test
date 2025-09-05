Feature: Registration
  As a new visitor
  I want to create an account
  So I can log in and use LinkMyGear

  Background:
    Given I navigate to "https://dev.linkmygear.com/register"
    And I wait for the page to be ready

  @auth @registration @smoke
  Scenario Outline: Successful registration with valid data
    When I fill "First name" with "<first_name>"
    And I fill "Last name" with "<last_name>"
    And I fill "Email" with "<email>"
    And I fill "Password" with "<password>"
    And I fill "Confirm Password" with "<password>"
    And I check the checkbox "I agree to the Terms"
    And I click the button "Create Account"
    Then I should be redirected to a page with URL containing "/verify" or "/dashboard"
    And I should see text containing "verify" or "welcome"

    Examples:
      | first_name | last_name | email                    | password       |
      | Test       | User      | <unique+timestamp@test.com> | StrongPass!123 |

  @auth @registration
  Scenario Outline: Registration validation errors for invalid inputs
    When I fill "First name" with "<first_name>"
    And I fill "Last name" with "<last_name>"
    And I fill "Email" with "<email>"
    And I fill "Password" with "<password>"
    And I fill "Confirm Password" with "<confirm>"
    And I click the button "Create Account"
    Then I should see a validation message for "<field_with_error>"

    Examples:
      | first_name | last_name | email              | password   | confirm    | field_with_error     |
      |            | User      | user@test.com      | Strong123! | Strong123! | First name           |
      | Test       |           | user@test.com      | Strong123! | Strong123! | Last name            |
      | Test       | User      | not-an-email       | Strong123! | Strong123! | Email                |
      | Test       | User      | user@test.com      | short      | short      | Password             |
      | Test       | User      | user@test.com      | Strong123! | Strong123  | Confirm Password     |

  @auth @registration
  Scenario: Registration requires terms agreement
    When I fill "First name" with "A"
    And I fill "Last name" with "B"
    And I fill "Email" with "terms-required@test.com"
    And I fill "Password" with "StrongPass!123"
    And I fill "Confirm Password" with "StrongPass!123"
    And I click the button "Create Account"
    Then I should see a validation message containing "Terms"
