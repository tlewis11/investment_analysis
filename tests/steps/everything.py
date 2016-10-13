import urllib2

@given("The service is running")
def step_impl(context):
    pass

@when('I request an api endpoint')
def step_impl(context):
    context.service_url = 'http://localhost:8080/dividends'
    url = context.service_url
   
 
    fp = urllib2.urlopen(url)
    context.status_code = fp.getcode()



@then('The service should be reachable')
def step_impl(context):
    assert context.status_code is 200



@then('I should get a json response')
def step_impl(context):
    pass


