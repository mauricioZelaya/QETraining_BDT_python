from utils.utils import *
from compare import expect
from behave import when, then
import logging
import time

logging.basicConfig(filename='..\logs\projects.log', level=logging.INFO)

@when(u'I send a {method} for projects request to {service} with {format} format')
def step_impl(context, method, service, format):
    context.method = method
    context.service = service
    context.format = format
    logging.info(logging.info(time.strftime("%c")+ ' - Method:'+ repr(context.method)))

@then(u'I should get the project status code {status_code}')
def step_impl(context, status_code):
    context.status_code =status_code
    context.endpoint = create_endpoint(context.endpoint, context.service)
    context.authorization = fill_authorization_basic(context.__DAN_USER__, context.__DAN_PASS__)
    expect(int(status_code)).to_equal(get_conn(context.endpoint, context.method, auth = context.authorization))
    logging.info(logging.info(time.strftime("%c")+ ' - Status code obtained:'+ repr(context.status_code)))

@when(u'I {method} the following body in {format} format to add the project with name {name}')
def step_impl(context, method, name, format):
    context.auth = fill_authorization_basic(context.__DAN_USER__, context.__DAN_PASS__)
    context.method = method
    context.projectName = name
    context.service = "projects"
    context.payload = {"Content": name}
    context.format = format

    context.endpoint = create_endpoint(context.endpoint, context.service)
    logging.info(time.strftime("%c")+ ' -  Endpoint created:'+ context.endpoint)

    context.response = get_response(context.endpoint, context.method, context.payload, context.auth)
    logging.info(time.strftime("%c")+ ' -  The following project: '+  context.projectName + " is added successfully.")

@then(u'I get project code result {code:d}')
def step_impl(context,code):
    context.auth = fill_authorization_basic(context.__DAN_USER__, context.__DAN_PASS__)
    expect(int(code)).to_equal(get_conn(context.endpoint, context.method,context.auth))

@then(u'the project with {name} is added.')
def step_impl(context, name):
    context.name = name
    print("IDRESPONSE:", context.response['Id'])
    varId= context.response['Id']
    print(context.name)
    isProjectByName= is_project_in_the_response( name, context.response)
    IsProjectById=is_project_in_the_response( varId, context.response)
    print(isProjectByName, "***********************")
    print(IsProjectById, "***********************")
    expect(True).to_equal(isProjectByName)
    expect(True).to_equal(IsProjectById)
