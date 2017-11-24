import requests
import json


def create_endpoint(*args):
    """
    This method will create a url as endpoint with many inputs.
    :param args: Arguments that will be included in the URL.
    :return: A URL as string.
    """
    endpoint = ''
    for arg in args:
        endpoint = endpoint + str(arg) + "/"
    endpoint = endpoint[:-1]
    endpoint = endpoint + ".json"
    return endpoint

def is_item_in_the_response(key, value, jsonResponse):
    """
    This method return true or false if the item is in the json response.
    :param value: The item that will be search.
    :param jsonResponse: The response in json format.
    :return: True or False
    """
    flag = False
    for item in jsonResponse:
        if type(jsonResponse[item]) == int:
            if item == key and jsonResponse[item] == int(value):
                flag = True

        if type(jsonResponse[item]) == str:
            if item == key and jsonResponse[item] == str(value):
                flag = True

        if type(jsonResponse[item]) == bool:
            if item == key and jsonResponse[item] == bool(value):
                flag = True
        else:
            #log and error
            pass
    return flag


def get_conn(endpoint, method="GET", json_data=None, headers=None, auth=None):
    """
    This method will set a connection to the endpoint, service and using the requested method.
    :param endpoint: URL endpoint.
    :param json_data: Payload to send.
    :param auth: The authorization credentials.
    :return: the response code
    """
    request = requested_method(endpoint, method=method, json_data=json_data, headers=headers, auth=auth)
    return request.status_code


def get_response(endpoint, method, json_data=None, auth=None):
    """
    This method execute a request and return the request in json format.
    :param endpoint: URL endpoint.
    :param method: Method will be used.
    :param json_data: Payload to execute.
    :param auth: The authorization credentials.
    :return: A request in json format.
    """
    request = requested_method(endpoint, method=method, json_data=json_data, auth=auth)
    return request.json()



def requested_method(endpoint, json_data=None, method="GET", headers=None, auth=None):
    """
    This method will return the request according the method sent
    :param endpoint: endpoint where we wil send the request
    :param json_data: parameters required in the request
    :param method: method selected to perform the request
    :param headers: any additional header
    :param auth: The authorization credentials.
    :return: None
    """
    if method == 'GET':
        return requests.get(endpoint, json_data, auth=auth)
    elif method == 'POST':
        return requests.post(endpoint, json=json_data, auth=auth)
    elif method == 'PUT':
        return requests.put(endpoint, json=json_data, auth=auth)
    elif method == 'DELETE':
        return requests.delete(endpoint, auth=auth)
    else:
        #log and error here on debugger declaring that no method was found
        pass


def fill_authorization_basic(user, pass_word):
    """
    This method fill the authorization for basic security
    :param user: The user nickname or mail.
    :param pass_word: The password of the user.
    :return: A tuple with the credentials.
    """
    return user, pass_word


def is_project_in_the_response(projectComponent, response):
    """
    This method return true or false if the name project is in the json response.
    :param projectComponent: The project component that will be search.
    :param response: The response.
    :return: True or False
    """
    for project in response:
        if response[project] == projectComponent:
            return True
    return False
