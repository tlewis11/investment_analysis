Feature: The service should be running and reachable by http
 
    Scenario: client consumes the service
        Given The service is running
        When I request an api endpoint
        Then The service should be reachable 
        Then I should get a json response
