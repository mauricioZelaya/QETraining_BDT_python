from utils.utils import *
from compare import expect
from behave import when, then
import logging


logging.basicConfig(filename='..\logs\projects.log', level=logging.INFO)

@when(u'I send a {method} for projects request to {service} with .json format')
def step_impl(context, method, service):
    context.method = method
    context.service = service

@then(u'Getting status code project operation {code}')
def step_impl(context, code):
    context.endpoint = create_endpoint(context.endpoint, context.service)
    authorization = fill_authorization_basic(context.__DAN_USER__, context.__DAN_PASS__)
    expect(int(code)).to_equal(get_conn(context.endpoint, context.method, auth=authorization))

@when(u'I {method} the following body in {format} format to add the project with name {name}')
def step_impl(context, method, name, format):
    authorization = fill_authorization_basic(context.__DAN_USER__, context.__DAN_PASS__)
    context.method = method
    context.projectName = name
    context.service = "projects"
    context.payload = {"Content": name}
    context.format = format
    logging.info('------------endpoint---------------')
    context.endpoint = create_endpoint(context.endpoint, context.service)
    logging.info(context.endpoint)
    logging.info('----------------payload-----------')
    logging.info(repr(context.payload))
    new_project = requested_method(context.endpoint, context.payload, context.method,auth=authorization)
    logging.info('----------------project-----------')
    logging.info(repr(new_project))

@then(u'I get project code result 200')
def step_impl(context):
    pass


@then(u'the new project is added.')
def step_impl(context):
    pass
