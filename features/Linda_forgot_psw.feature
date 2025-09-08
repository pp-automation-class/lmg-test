Here’s a feature file you can save as Linda_forgot_psw.feature.

```gherkin
Feature: Linda forgot password
  As Linda who forgot her password
  I want to request a password reset
  So I can regain access to my account

  Background:
    Given I navigate to "{{RESET_PAGE_URL}}"
    And I wait for the page to be ready

  @auth @password @smoke
  Scenario: Linda requests a password reset with a registered email
    When I fill "Email" with "{{REGISTERED_EMAIL}}"
    And I click the button "Send reset link"
    Then I should see a success message containing "email" or "sent"
```
# Created by m-ele at 9/8/2025
Feature: # Enter feature name here
  # Enter feature description here

  Scenario: # Enter scenario name here
    # Enter steps here