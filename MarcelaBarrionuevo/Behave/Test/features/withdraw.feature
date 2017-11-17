Feature: Withdraw fixed amount
The 'Withdraw cash' menu contains several fixed amounts to
speed up a transaction for user
  
  Scenario: Withdraw fixed amount of $50
    Given I have $500 in my Account
	When I choose to withdraw the fixed amount of $50
	Then I should receive $50 cash
	And the balance of my account should be $450

  Scenario: Withdraw fixed amount of $100
    Given I have $500 in my Account
	When I choose to withdraw the fixed amount of $100
	Then I should receive $100 cash
	And the balance of my account should be $400
	
  Scenario: Withdraw fixed amount of $200
    Given I have $500 in my Account
	When I choose to withdraw the fixed amount of $200
	Then I should receive $200 cash
	And the balance of my account should be $300

  Scenario: Withdraw fixed amount of $300
    Given I have $500 in my Account
	When I choose to withdraw the fixed amount of $300
	Then I should receive $300 cash
	And the balance of my account should be $200
