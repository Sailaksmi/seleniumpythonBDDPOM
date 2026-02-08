Feature: Login functionality of Demo Web Shop
  As a registered user
  I want to login to the application
  So that I can access my account features


Scenario Outline: Verify login functionality with different credentials
  Given the user is on the Demo Web Shop home page
  And user navigates to Login page
  When user enters email "<email>"
  And user enters password "<password>"
  And user clicks on Login button
  Then the user should be logged in successfully


Examples:
  | email                   | password     | 
  | ananyasingh3@test.com   | Test@123     | 
