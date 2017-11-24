from utils.utils import *
from compare import expect

######## _PUT TESTS_ #######

@given('I get an {itemId:d} to modify')
def step_impl(context, itemId):
    context.itemId = itemId

@given('I get a {parameter} to modify')
def step_impl(context, parameter):
    context.parameter = parameter

@given('I also get a {value} to modify')
def step_impl(context, value):
    context.value = value

@when('I make the {method} request')
def step_impl(context, method):
    context.method =  method
    context.authorization = fill_authorization_basic(context.__ALEJANDRO_USER__, context.__ALEJANDRO_PASS__)
    context.endpoint = create_endpoint(context.endpoint, context.service, str(context.itemId))
    context.jsonData = {context.parameter: context.value}
    context.response = get_response(context.endpoint, context.method, context.jsonData, context.authorization)


@then('I verify that the parameter has change in the response')
def step_impl(context):
    expect(True).to_equal(is_item_in_the_response(context.parameter, context.value, context.response))





######## _GET TESTS_ #######


@given(u'I get a {service}')
def step_impl(context, service):
    context.service = service

@when(u'I also get a {method} to validate')
def step_impl(context, method):
    context.method =  method

@when('I get an {itemId:d} to search')
def step_impl(context, itemId):
    context.itemId = itemId
    context.endpoint = create_endpoint(context.endpoint, context.service, context.itemId)

@then('I get the {code:d} response to validate')
def step_impl(context, code):
    context.authorization = fill_authorization_basic(context.__ALEJANDRO_USER__, context.__ALEJANDRO_PASS__)
    expect(code).to_equal(get_conn(context.endpoint, context.method, auth = context.authorization))


@then('I verify the {itemKey} in the response')
def step_impl(context, itemKey):
    context.itemKey = itemKey
    context.response = get_response(context.endpoint, context.method, auth = context.authorization)
    expect(True).to_equal(is_item_in_the_response(context.itemKey, context.itemId, context.response))



