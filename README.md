# LMG Test Automation Project

Automated testing framework using Behave (BDD) and Playwright for web application testing.

## Prerequisites

- Python 3.8 or higher
- Poetry (for dependency management)
- Git

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/pp-automation-class/lmg-test.git
cd lmg-test
```

### 2. Install Poetry (if not already installed)

```bash
# On macOS/Linux using curl
curl -sSL https://install.python-poetry.org | python3 -

# On Windows using PowerShell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

### 3. Install project dependencies

```bash
# Install all dependencies from pyproject.toml
poetry install
```

### 4. Install Playwright browsers

```bash
# Install required browsers for Playwright
poetry run playwright install
```

### 5. Activate the virtual environment

```bash
# Activate Poetry shell
poetry shell
```

## Project Structure

```
lmg-test/
├── features/              # BDD feature files
│   └── login_page.feature # Login page test scenarios
├── environment.py         # Behave configuration
├── pyproject.toml        # Project dependencies
├── poetry.lock           # Locked dependency versions
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

## Running Tests

### Run all tests

```bash
poetry run behave
```

### Run specific feature

```bash
poetry run behave features/login_page.feature
```

### Run tests with specific tags

```bash
# Run only smoke tests
poetry run behave --tags=@smoke

# Run login tests but exclude negative tests
poetry run behave --tags=@login --tags=~@negative
```

### Generate test reports

```bash
# Generate JUnit XML report
poetry run behave --junit

# Generate JSON report
poetry run behave -f json -o reports/results.json
```

## Writing Tests

Tests are written in Gherkin syntax in `.feature` files. Example:

```gherkin
Feature: Login Page
  
  Scenario: Successful login
    Given I am on the login page
    When I enter valid credentials
    And I click the login button
    Then I should be redirected to the dashboard
```

## Dependencies

- **behave**: BDD testing framework
- **playwright**: Browser automation library
- **pytest-playwright**: Pytest plugin for Playwright
- **pytest**: Testing framework
- **requests**: HTTP library

## Troubleshooting

### Poetry not found

Add Poetry to your PATH:
```bash
export PATH="$HOME/.local/bin:$PATH"
```

### Playwright browsers not installing

Try installing with additional dependencies:
```bash
poetry run playwright install --with-deps
```

### Permission errors

Ensure you have proper permissions:
```bash
chmod +x environment.py
```

## Contributing

1. Create a feature branch from `master`
2. Make your changes
3. Run tests to ensure nothing is broken
4. Create a pull request

## License

[Your License Here]