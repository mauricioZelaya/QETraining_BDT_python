from utils.utils import *
from compare import expect


@when('I need to test the response in the {service} method with {snippet} using {method}')
def step_impl(context, service, snippet = None, method = "GET"):
    context.method = method
    context.service =  service
    context.payload = fill_payload(context.apiKey)

@then('I get response with {code:d} code')
def step_impl(context, code):
    context.code = code
    expect(context.code).to_equal(get_conn(context.host, context.rootpath,
                                           context.service, context.method, context.payload))

@when('I have to use a {keyword} to search')
def step_impl(context, keyword):
    context.keyword = keyword

@then('A {key} of response equals to {value}')
def step_impl(context, value, key):
    j_response = get_response(context.host, context.rootpath,
                              context.service, context.method, context.payload)
    expect(value).to_equal(j_response[key])




