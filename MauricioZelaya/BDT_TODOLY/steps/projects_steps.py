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
    logging.info(logging.info(time.strftime("%c")+ ' - 1 -  Method sent:'+ repr(context.method)))

@then(u'I should get the project status code {status_code}')
def step_impl(context, status_code):
    context.status_code =status_code
    context.endpoint = create_endpoint(context.endpoint, context.service)
    context.authorization = fill_authorization_basic(context.__DAN_USER__, context.__DAN_PASS__)
    expect(int(status_code)).to_equal(get_conn(context.endpoint, context.method, auth = context.authorization))
    logging.info(logging.info(time.strftime("%c")+ ' - 2 - Status code obtained:'+ repr(context.status_code)))

@when(u'I {method} the following body in {format} format to add the project with name {name}')
def step_impl(context, method, name, format):
    context.auth = fill_authorization_basic(context.__DAN_USER__, context.__DAN_PASS__)
    context.method = method
    context.projectName = name
    context.service = "projects"
    context.payload = {"Content": name}
    context.format = format

    context.endpoint = create_endpoint(context.endpoint, context.service)
    logging.info(time.strftime("%c")+ ' - 3 - Endpoint created:'+ context.endpoint)

    context.response = get_response(context.endpoint, context.method, context.payload, context.auth)
    logging.info(time.strftime("%c")+ ' - 3 - The following project: '+  context.projectName + " name is added successfully.")

@then(u'the project with {name} is added.')
def step_impl(context, name):
    context.name = name
    projectId= context.response['Id']

    isProjectByName= is_project_in_the_response( name, context.response)
    isProjectById= is_project_in_the_response( projectId, context.response)

    expect(True).to_equal(isProjectByName)
    logging.info(time.strftime("%c") + ' - 4 - Verification 1 project By Name: is ' + str(isProjectByName))
    expect(True).to_equal(isProjectById)
    logging.info(time.strftime("%c") + ' - 5 - Verification 2 Project By Id: is ' + str(isProjectById))

@when(u'I {method} the following body in {format} format to update the project with icon: {iconId}')

def step_impl(context, iconId, method, format):

    context.authorization = fill_authorization_basic(context.__DAN_USER__, context.__DAN_PASS__)
    context.service = "projects"

    enpointUpdate = create_endpoint(context.endpoint, context.service)
    context.response = get_response(enpointUpdate, "POST", {"Content": "project0"}, context.authorization)
    projectId = context.response['Id']

    enpointUpdate2 = create_endpoint(context.endpoint, context.service+"/"+str(projectId))
    context.payload = {"Content": "My updated project","Icon": iconId}
    context.method = method
    context.response = get_response(enpointUpdate2, context.method,context.payload, context.authorization)

    isProjectById = is_project_in_the_response(projectId, context.response)

    expect(True).to_equal(isProjectById)
    logging.info(time.strftime("%c") + ' - 6 -  Project updated By Id: is ' + str(isProjectById))

@then(u'the project with the new icon {iconId} updated.')
def step_impl(context,iconId):
    context.iconId = iconId

    expect(context.payload['Icon']).to_equal(context.payload['Icon'])
    logging.info(time.strftime("%c") + ' - 7 - Verification Porject updated')


@then(u'I get project code result 200')
def step_impl(context):
    pass
