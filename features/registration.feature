Feature: User Registration
  As a new user
  I want to register on Demo Web Shop
  So that I can create an account successfully

@positive @smoke @sanity @registration @regression
  Scenario Outline: Successful user registration with valid details
    Given the user is on the Demo Web Shop home page
    When the user clicks on the "Register" link
    And the user selects gender as "<gender>"
    And the user enters first name "<firstName>"
    And the user enters last name "<lastName>"
    And the user enters email "<email>"
    And the user enters password "<password>"
    And the user enters confirm password "<confirmPassword>"
    And the user clicks on the Register button
    Then the user should see the registration success message

    Examples:
      | gender | firstName | lastName | email                  | password  | confirmPassword |
      | Female | Ananya    | Singh    | auto_email     | Test@123  | Test@123        |

   @negative @sanity @registration @regression
Scenario: User registration should fail if email already exists

    Given the user is on the Demo Web Shop home page
    When the user registers with valid details
    And the user tries to register again with the same email
    Then the user should see the registration failure message
