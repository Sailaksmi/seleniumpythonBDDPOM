Feature: Checkout billing address

  As a logged-in user
  I want to enter billing address details
  So that I can proceed with checkout successfully

  @regression @checkout
  Scenario Outline: Enter address and continue checkout
    Given user naviagtes to checkoutpage with "<email>", "<password>", and select "<category>", "<sortOrder>", "<bookName>"
    And user should accept terms and conditions
    And user proceeds to checkout
    When user fills all billing details and proceed to checkout "<company>", "<country>", "<state>", "<city>", "<address1>", "<address2>", "<zipCode>", "<phone>", "<fax>"
    Then the user should see the "Log out" link

    Examples:
      | email | password | category | sortOrder | bookName | company | country | state | city | address1 | address2 | zipCode | phone | fax |
      | ananyasingh3@test.com | Test@123 | Books | Price: Low to High | Health Book | Test | India | Other (Non US) | Hyderabad | Ameerpet Road | 2nd lane | 500016 | 9876543210 | 897789786 |
