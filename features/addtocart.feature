Feature: Add book to shopping cart after sorting by price

  As a logged-in user
  I want to sort books by low to high price
  And add a selected book to the shopping cart
  So that I can purchase the book successfully

 @regression @addtocart
Scenario Outline: Add book to cart after sorting books by low to high price
  Given the user is on the Demo Web Shop home page
  When the user registers with valid details
  And the user logs in with the same registered details
  And user navigates to the "<category>" category
  And user sorts the books by "<sortOrder>"
  And user selects the book "<bookName>"
  When user clicks on Add to Cart button
  Then the book "<bookName>" should be added to the shopping cart
  And shopping cart count should be updated

Examples:
  | category | sortOrder           | bookName     | 
  | Books    |   Price: Low to High  | Health Book  | 
