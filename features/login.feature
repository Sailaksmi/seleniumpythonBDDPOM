Feature: Login functionality of Demo Web Shop
  As a registered user
  I want to login to the application
  So that I can access my account features

@positive @smoke @sanity @regression @login
Scenario Outline: Verify login functionality with valid credentials
  Given the user is on the Demo Web Shop home page
  And user navigates to Login page
  When user enters email "<email>"
  And user enters password "<password>"
  And user clicks on Login button
  Then the user should be logged in successfully


Examples:
  | email                   | password     | 
  | ananyasingh3@test.com   | Test@123     | 

@negative @sanity @regression @login
Scenario Outline: Verify login functionality with invalid credentials
  Given the user is on the Demo Web Shop home page
  And user navigates to Login page
  When user enters email "<email>"
  And user enters password "<password>"
  And user clicks on Login button
  Then an error message should be displayed


Examples:
  | email                   | password     | 
  | test@test.com  |   Test@123  |
| ananyasingh3@test.com   | Tet@123     | 