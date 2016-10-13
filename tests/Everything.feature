Feature: The service should be running and reachable by http
 
    Scenario: client consumes the service
        Given The service is running
        When I request an api endpoint
        Then The service should be reachable 
        Then I should get a json response


    Scenario: I want to get a current dividend for a company
        Given I format my request correctly    
        When I request dividend for the stock symbol
        Then I should get a json response object including the current dividend
