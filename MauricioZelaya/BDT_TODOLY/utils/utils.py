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

def is_item_in_the_response(key, itemId, jsonResponse):
    """
    This method return true or false if the item is in the json response.
    :param itemId: The item that will be search.
    :param jsonResponse: The response in json format.
    :return: True or False
    """
    for item in jsonResponse:
        print(jsonResponse[item])
        if jsonResponse[item] == itemId:
            return True
    return False


def get_conn(endpoint, method="GET", payload=None, headers=None, auth=None):
    """
    This method will set a connection to the endpoint, service and using the requested method.
    :param endpoint: URL endpoint.
    :param payload: Payload to send.
    :param auth: The authorization credentials.
    :return: the response code
    """
    request = requested_method(endpoint, method=method, payload=payload, headers=headers, auth=auth)
    return request.status_code


def get_response(endpoint, method, payload=None, auth=None):
    """
    This method execute a request and return the request in json format.
    :param endpoint: URL endpoint.
    :param method: Method will be used.
    :param payload: Payload to execute.
    :param auth: The authorization credentials.
    :return: A request in json format.
    """
    request = requested_method(endpoint, method=method, payload=payload, auth=auth)
    return request.json()



def requested_method(endpoint, payload=None, method="GET", headers=None, auth=None):
    """
    This method will return the request according the method sent
    :param endpoint: endpoint where we wil send the request
    :param payload: parameters required in the request
    :param method: method selected to perform the request
    :param headers: any additional header
    :param auth: The authorization credentials.
    :return: None
    """
    if method == 'GET':
        return requests.get(endpoint, payload, auth=auth)
    elif method == 'POST':
        return requests.post(endpoint, json=payload, auth=auth)
    elif method == 'PUT':
        return requests.put(endpoint, json=payload, auth=auth)
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
        print(response[project])
        if response[project] == projectComponent:
            return True
    return False
