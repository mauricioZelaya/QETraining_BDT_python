from utils.utils import *
from compare import expect
from behave import when, then

@when(u'I send the {service} with the {format}')
def step_impl(context, service, format):
    context.service = service
    context.format = format

@when(u'I used the {method}')
def step_impl(context, method):
    context.method = method

@then(u'I get the response with {code:d} code')
def step_impl(context, code):
    authorization = fill_authorization_basic(context.__DENNIS_USER__, context.__DENNIS_PASS__)
    expect(int(code)).to_equal(get_conn(context.host, context.rootpath,
                                   context.service, context.format, context.method, auth = authorization))
