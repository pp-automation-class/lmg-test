Feature: Login
  As a registered user
  I want to log into LinkMyGear
  So I can access my account and dashboard

  Background:
    Given I navigate to "https://dev.linkmygear.com/login"
    And I wait for the page to be ready

  @auth @login @smoke
  Scenario Outline: Successful login with valid credentials
    When I fill "Email" with "<email>"
    And I fill "Password" with "<password>"
    And I click the button "Sign In"
    Then I should be redirected to a page with URL containing "/dashboard"
    And I should see text "Dashboard"

    Examples:
      | email                 | password       |
      | <replace@test.com>    | <replace_me1>  |

  @auth @login
  Scenario Outline: Login fails with invalid credentials
    When I fill "Email" with "<email>"
    And I fill "Password" with "<password>"
    And I click the button "Sign In"
    Then I should see an error message containing "Invalid" or "incorrect" or "failed"

    Examples:
      | email                 | password      |
      | not-registered@test.com | wrong-pass  |

  @auth @login
  Scenario: Login form validation prevents submit with empty fields
    When I click the button "Sign In"
    Then I should see a validation message for "Email"
    And I should see a validation message for "Password"

  @auth @login
  Scenario: Login page has accessible links for sign up and password recovery
    Then I should see link "Sign Up"
    And I should see link "Forgot Password?"
    When I click the link "Sign Up"
    Then I should be redirected to a page with URL containing "/register"
    When I navigate back
    And I click the link "Forgot Password?"
    Then I should be redirected to a page with URL containing "/password/reset"
