from utils.utils import *
from compare import expect

@given(u'I get a {service}')
def step_impl(context, service):
    context.service = service

@when(u'I also get a {method} to validate')
def step_impl(context, method):
    context.method =  method

@when('I get an {itemId:d} to search')
def step_impl(context, itemId):
    context.itemId = itemId

@when(u'I get a {format} that I want for the response to validate')
def step_impl(context, format):
    context.format = format
    endpoint = create_endpoint(context.host, context.rootpath,
                                           context.service, context.itemId)
    print(endpoint)
    print(endpoint)

@then(u'I get the {code:d} response to validate')
def step_impl(context, code):
    authorization = fill_authorization_basic(context.__ALEJANDRO_USER__, context.__ALEJANDRO_PASS__)
    expect(code).to_equal(get_conn(context.host, context.rootpath,
                                           context.service, context.format, context.method, auth = authorization))

