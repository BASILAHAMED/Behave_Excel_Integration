Feature: SauceDemo login validation using Excel data

  Scenario: Login with multiple credentials
    Given the Excel file is loaded
    When I try to login with all data sets
    Then the login results should be written back to Excel
