Feature: Checkout billing address

  As a logged-in user
  I want to enter billing address details
  So that I can proceed with checkout successfully

@regression @checkout
  Scenario Outline: Enter address and continue checkout
    Given the user is on the Demo Web Shop home page
    When the user registers with valid details
    And the user logs in with the same registered details
    And the user selects "<category>", sorts by "<sortOrder>", and chooses "<bookName>"
    And user should accept terms and conditions
    And user proceeds to checkout
    When user fills all billing details and proceed to checkout "<company>", "<country>", "<state>", "<city>", "<address1>", "<address2>", "<zipCode>", "<phone>", "<fax>"
    Then the user should see the "Log out" link

    Examples:
       | category | sortOrder | bookName | company | country | state | city | address1 | address2 | zipCode | phone | fax |
       | Books | Price: Low to High | Health Book | Test | India | Other (Non US) | Hyderabad | Ameerpet Road | 2nd lane | 500016 | 9876543210 | 897789786 |
