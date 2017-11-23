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
    for item in jsonResponse:
        value_t = value_type(jsonResponse[item])
        if value_t == "int":
            if item == key and jsonResponse[item] == int(value):
                return True

        if value_t == "str":
            if item == key and jsonResponse[item] == str(value):
                return True

        if value_t == "bool":
            if item == key and jsonResponse[item] == bool(value):
                return True
        else:
            #log and error
            pass
    return False

def value_type(value):
    """
    This method will determine a type of value that is send.
    :param value: The value that will be tested.
    :return: The type of the value in a string
    """
    if type(value) == int:
        return "int"
    if type(value) == str:
        return "str"
    if type(value) == bool:
        return "bool"
    else:
        #log an error
        pass


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
        return requests.post(endpoint, json_data, headers)
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

