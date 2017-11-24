from utils.utils import *
from compare import expect

@given(u'I have connection to "{host}"')
def step_impl(context, host):
    context.endpoint = host

@given(u'a {roothpath}')
def step_impl(context, roothpath):
    context.rootpath = roothpath

@when(u'I connect to youtube')
def step_impl(context):
    pass

@then(u'I receive status code {status}')
def step_impl(context, status):
    payload={"key": context.apiKey, "parentId": "z13icrq45mzjfvkpv04ce54gbnjgvroojf0", "part": "snippet"}
    currentStatusCode = get_conn(context.host, context.rootpath, '/comments', payload)
    expect(currentStatusCode).to_equal(int(status))
