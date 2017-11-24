from utils.utils import *
from compare import expect
from behave import when, then

##### List Items ######

@when(u'I send the {service}')
def step_impl(context, service):
    context.service = service

@when(u'I used the {method}')
def step_impl(context, method):
    context.method = method

@then(u'I get the response with {code:d} code')
def step_impl(context, code):
    context.endpoint = create_endpoint(context.endpoint, context.service)
    authorization = fill_authorization_basic(context.__DENNIS_USER__, context.__DENNIS_PASS__)
    expect(code).to_equal(get_conn(context.endpoint, context.method, auth=authorization))


##### Delete from a Item ######

@given(u'A {service} and a {method}')
def step_impl(context, service, method):
    context.service = service
    context.method = method

@when(u'I select a {id:d} of the item')
def step_impl(context, id):
    context.id = id
    context.endpoint = create_endpoint(context.endpoint, context.service, context.id)

@then(u'I get the result equals to {code:d}')
def step_impl(context, code):
    context.authorization = fill_authorization_basic(context.__DENNIS_USER__, context.__DENNIS_PASS__)
    expect(code).to_equal(get_conn(context.endpoint, context.method, auth=context.authorization))

@then(u'I verify if the {itemkey} is correctly dislpayed in the response')
def step_impl(context, itemkey):
    context.itemkey = itemkey
    context.response = get_response(context.endpoint, context.method, auth=context.authorization)
    expect(True).to_equal(is_item_in_the_response(context.itemkey, context.id, context.response))



##### Root of a Item ######

@given(u'that i have the {service} and the {method}')
def step_impl(context, service, method):
    context.service = service
    context.method = method

@when(u'I optained a {iditem} with the {rootitem} of Item')
def step_impl(context, iditem, rootitem):
    context.iditem = iditem
    context.rootitem = rootitem
    context.endpoint = create_endpoint(context.endpoint, context.service, context.iditem, context.rootitem)
    #print(context.endpoint)

@then(u'I get the status {code:d}')
def step_impl(context, code):
    context.authorization = fill_authorization_basic(context.__DENNIS_USER__, context.__DENNIS_PASS__)
    expect(code).to_equal(get_conn(context.endpoint, context.method, auth=context.authorization))

@then(u'I review if the {itemidkey} is correctly in the response')
def step_impl(context, itemidkey):
    context.itemidkey = itemidkey
    context.response = get_response(context.endpoint, context.method, auth=context.authorization)
    expect(True).to_equal(is_item_in_the_response(context.itemidkey, context.iditem, context.response))



