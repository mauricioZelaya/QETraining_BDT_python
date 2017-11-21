from utils.utils import *
from compare import expect


@when(u'I send a {method} request to {service} with {format} format')
def step_impl(context, method, service, format):
    context.method = method
    context.service = service
    context.format = format


@then(u'I get status code {code}')
def step_impl(context, code):
    auth = fill_authorization_basic(context.__MAURICIO_USER__, context.__MAURICIO_PASS__)
    statusCodeReceived = get_conn(context.host, context.rootpath, context.service, context.format, context.method, auth=auth)
    expect(statusCodeReceived).to_equal(int(code))
