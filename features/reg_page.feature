Feature: Reg page test
	
	Scenario: Check if the registration page is really a registration page
		Given Ticketscloud new partner registration page
		When Select registration 
		Then Registration page opens

