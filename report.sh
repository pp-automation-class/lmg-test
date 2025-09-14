#!/bin/bash

# Allure Report Generator and Server Script
# This script generates and opens the Allure report for BDD test results

set -e  # Exit on any error

echo "🚀 Generating Allure Report..."

# Generate fresh report from allure-results
if [ -d "allure-results" ]; then
    echo "📊 Found allure-results directory"
    allure generate allure-results --clean -o allure-report
    echo "✅ Report generated successfully"
else
    echo "❌ No allure-results directory found. Please run tests first with Allure formatter:"
    echo "   poetry run behave features/maps.feature -f allure_behave.formatter:AllureFormatter -o allure-results"
    exit 1
fi

echo "🌐 Opening Allure report in browser..."
allure open allure-report