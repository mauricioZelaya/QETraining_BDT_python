from utils.utils import *
from compare import expect


@given(u'{vID} video id for a comment thread')
def step_impl(context, vID):
    context.videoID = vID


@when(u'I send a {method} comment threads list using {service}')
def step_impl(context, method, service):
    context.method = method
    context.service = service


@then(u'status code {code} is received')
def step_impl(context, code):
    payload = {"key": context.apiKey, "videoId": context.videoID, "part": "snippet"}
    currentStatusCode = get_conn(context.host, context.rootpath, context.service, context.method, payload)
    expect(currentStatusCode).to_equal(int(code))

@given(u'{Json_body} body')
def step_impl(context, Json_body):
    context.body = Json_body

@when(u'I {the_method} the comment using {the_service} service')
def step_impl(context,the_method, the_service):
    context.method = the_method
    context.service = the_service

@then(u'get {code}')
def step_impl(context, code):
    payload = {"key": context.apiKey, "part": "snippet"}
    currentStatusCode = get_conn(context.host, context.rootpath, context.service, context.method, payload, context.body)
    expect(currentStatusCode).to_equal(int(code))

