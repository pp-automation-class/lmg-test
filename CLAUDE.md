# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Important Guidelines

### Code Style Requirements
1. **Keep code as simple as possible** - This is a learning project. Avoid complex patterns or over-engineering.
2. **Educational focus** - Code is written for learning purposes. Prioritize clarity and readability over performance optimizations.
3. **Use short, descriptive comments** - Add brief comments to explain what code does, especially for learning concepts.

## Project Overview

This is a BDD test automation framework using Behave and Playwright for web application testing. The project uses Poetry for dependency management and follows the Gherkin syntax for test scenarios.

## Key Commands

### Setup and Installation
```bash
# Install dependencies
poetry install

# Install Playwright browsers
poetry run playwright install

# Activate virtual environment
poetry shell
```

### Running Tests
```bash
# Run all tests
poetry run behave

# Run specific feature file
poetry run behave features/login_page.feature

# Run tests with specific tags
poetry run behave --tags=@smoke
poetry run behave --tags=@login --tags=~@negative

# Run with JUnit report
poetry run behave --junit

# Run with JSON report
poetry run behave -f json -o reports/results.json

# Dry run (validate scenarios without execution)
poetry run behave --dry-run

# Run specific scenario by line number
poetry run behave features/login_page.feature:9
```

## Architecture and Structure

### Test Framework Architecture
- **BDD Framework**: Behave for behavior-driven development
- **Browser Automation**: Playwright for cross-browser testing
- **Test Structure**: Gherkin feature files define test scenarios
- **Environment Hooks**: environment.py provides test lifecycle hooks (before/after scenario, feature, step)

### Directory Structure
- `features/`: Contains all .feature files with BDD scenarios
- `environment.py`: Behave configuration and test hooks
- `pages/`: Page Object Model classes (currently empty, to be implemented)
- `steps/`: Step definitions for feature files - ALL step definitions should be created here with descriptive file names matching the feature they support
- `utils/`: Utility functions and helpers (currently empty, to be implemented)

### Step Definitions
- **Location**: All step definitions MUST be created in the `steps/` directory
- **File Naming**: Use descriptive names that match the feature (e.g., `login_steps.py`, `registration_steps.py`)
- **Decorator Usage**: Use ONLY `@step` decorator to define steps (not `@given`, `@when`, `@then`)
- **Context Usage**: Access browser and page through `context.page` set up in environment.py
- **Reusability**: Create reusable step definitions that can be shared across features

### Feature Files Pattern
All feature files follow a consistent naming convention with prefixes indicating the contributor:
- `am_*.feature`: Feature files from contributor AM
- `ab_*.feature`: Feature files from contributor AB
- `anKr_*.feature`: Feature files from contributor AnKr
- Base `login_page.feature`: Original feature file

### Test Tags
Common tags used across features:
- `@smoke`: Critical path tests
- `@login`: Login functionality tests
- `@negative`: Negative test scenarios
- `@registration`: Registration tests
- `@logout`: Logout tests
- `@password-reset`: Password recovery tests

### Dependencies
Core dependencies managed by Poetry:
- `behave`: BDD test framework
- `playwright`: Browser automation
- `pytest` and `pytest-playwright`: Additional testing support
- Python 3.9+