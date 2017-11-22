from utils.utils import *
from compare import expect


@when(u'I send a {method} request to {service}')
def step_impl(context, method, service):
    context.method = method
    context.service = service
    context.endpoint = create_endpoint(context.endpoint, context.service)


@then(u'I get status code {code}')
def step_impl(context, code):
    if context.method == 'DELETE':
        auth = fill_authorization_basic('mago_astaroth@hotmail.com', '1234_')
    else:
        auth = context.auth
    statusCodeReceived = get_conn(context.endpoint, context.method, auth=auth)
    expect(statusCodeReceived).to_equal(int(code))


@given(u'{format} format for the response')
def step_impl(context, format):
    context.format = format


@when(u'I {method} the {service} service method to request user information')
def step_impl(context, method, service):
    context.method = method
    context.service = service
    context.endpoint = create_endpoint(context.endpoint, context.service)


@then(u'I receive status code {code}')
def step_impl(context, code):
    expect(get_conn(context.endpoint, context.method, auth=context.auth)).to_equal(int(code))



@then(u'I compare result')
def step_impl(context):
   # context.text = text
    response = get_response(context.endpoint, context.method, auth=context.auth)
    print(response)
    newJson = serialyze_json(response, 'zelaya.mauricio@gmail.com')
    print(newJson)
    #expect(response).to_equal(context.text)

