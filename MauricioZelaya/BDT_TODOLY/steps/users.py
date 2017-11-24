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


@given(u'an authenticated user {email} and {firstName} {lastName}')
def step_impl(context, email, firstName, lastName):
    context.email = email
    context.fullName = firstName + " " + lastName


@when(u'I {method} the {service} service method to request user information')
def step_impl(context, method, service):
    context.method = method
    context.service = service
    context.endpoint = create_endpoint(context.endpoint, context.service)


@then(u'I receive status code {code}')
def step_impl(context, code):
    expect(get_conn(context.endpoint, context.method, auth=context.auth)).to_equal(int(code))


@then(u'I compare result to validate the mail and fullname are aslo received')
def step_impl(context):
    context. response = get_response(context.endpoint, context.method, auth=context.auth)
    # print(context.email)
    # print(context.fullName)
    # print(context.response)
    expect(True).to_equal(is_item_in_the_response("Email", context.email, context.response))
    expect(True).to_equal(is_item_in_the_response("FullName", context.fullName, context.response))


@given(u'an authenticated user with {userEmail} email')
def step_impl(context, userEmail):
    context.Email = userEmail


@when(u'I {method} request to change the full name to {newFirstName} {newLastName} using {service} service')
def step_impl(context, method, newFirstName, newLastName, service):
    context.method = method
    context.service = service
    context.fullName = newFirstName + " " + newLastName
    context.json_data = {"Email": context.Email, "FullName": context.fullName}
    print(context.json_data)


@then(u'I get response code {code}')
def step_impl(context, code):
    context.endpoint = create_endpoint(context.endpoint, context.service)
    expect(get_conn(context.endpoint, method=context.method, json_data=context.json_data, auth=context.auth)).to_equal(int(code))


@then(u'The new name is part of the response')
def step_impl(context):
    context.response = get_response(context.endpoint, context.method, auth=context.auth)
    print(context.response)
    expect(True).to_equal(is_item_in_the_response("FullName", context.fullName, context.response))


