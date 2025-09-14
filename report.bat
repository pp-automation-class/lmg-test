@echo off
REM Allure Report Generator and Server Script for Windows
REM This script generates and opens the Allure report for BDD test results

setlocal enabledelayedexpansion

echo 🚀 Generating Allure Report...

REM Check if allure-results directory exists
if exist "allure-results" (
    echo 📊 Found allure-results directory
    allure generate allure-results --clean -o allure-report
    if !errorlevel! equ 0 (
        echo ✅ Report generated successfully
    ) else (
        echo ❌ Failed to generate report
        pause
        exit /b 1
    )
) else (
    echo ❌ No allure-results directory found. Please run tests first with Allure formatter:
    echo    poetry run behave features/maps.feature -f allure_behave.formatter:AllureFormatter -o allure-results
    pause
    exit /b 1
)

echo 🌐 Opening Allure report in browser...
allure open allure-report