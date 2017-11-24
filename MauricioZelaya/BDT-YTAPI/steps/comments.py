from utils.utils import *
from compare import expect


@given(u'{parent} parent id for a comment')
def step_impl(context, parent):
    context.parentID = parent


@when(u'I send a {themethod} comments list using {service}')
def step_impl(context, themethod, service):
    context.method = themethod
    context.APIService = service


@then(u'I get a status code {code}')
def step_impl(context, code):
    payload = {"key": context.apiKey, "parentId": context.parentID, "part": "snippet"}
    currentStatusCode = get_conn(context.host, context.rootpath, context.APIService, context.method, payload)
    expect(currentStatusCode).to_equal(int(code))
