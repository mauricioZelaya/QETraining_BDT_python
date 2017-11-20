from utils.utils import *
from compare import expect

@when(u'Test the response in the {service} using {method}')
def step_impl(context, service, method):
    context.service = service
    context.method = method

@when(u'selection the {video_id} id')
def step_impl(context, video_id):
    context.video_id = video_id
    context.payload = fill_payload(context.apiKey, videoId = context.video_id)


@then(u'The response with {response} code')
def step_impl(context, response):
    context.response = response
    print(context.host)
    print(context.rootpath)
    print(context.service)
    print(context.method)
    print(context.payload)
    expect(context.response).to_equal(get_conn(context.host, context.rootpath,
                                           context.service, context.method, payload = context.payload))


