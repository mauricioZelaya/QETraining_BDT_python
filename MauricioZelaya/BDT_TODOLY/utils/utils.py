import requests
import json


def create_endpoint(*args):
    endpoint = ''
    for arg in args:
        endpoint = endpoint + str(arg) + "/"
    endpoint = endpoint[:-1]
    endpoint = endpoint + ".json"
    return endpoint


def connect_to_api(endpoint, method="GET", payload=None, headers=None, auth=None):
    """
    method to get the connection from the API
    :param host: host to connect
    :param root_path: path to the api
    :param service: service to be requested
    :param format: format of the response xml or json
    :param method: method to be invoked GET, POST, PUT, DELETE
    :param payload: payload to send
    :param headers: additional headers if required
    :param auth: The authorization credentials
    :return: connection response to requested method
    """
    # endpoint = host + root_path + service + format
    return requested_method(endpoint, payload, method, headers, auth)

def get_conn(endpoint, method="GET", payload=None, headers=None, auth=None):
    """
    This method will set a connection to the endpoint, service and using the requested method.
    :param endpoint: URL endpoint.
    :param payload: Payload to send.
    :param auth: The authorization credentials.
    :return: the response code
    """
    request = connect_to_api(endpoint, method="GET", payload=None, headers=None, auth=None)
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
    request = connect_to_api(endpoint, method="GET", payload=None, headers=None, auth=None)
    print(auth)
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
        return requests.post(endpoint, payload, headers)
    elif method == 'PUT':
        return requests.put(endpoint, payload)
    elif method == 'DELETE':
        return requests.delete(endpoint, auth=auth)


def fill_authorization_basic(user, pass_word):
    return user, pass_word


def serialyze_json(fromJson, data):
    # print(fromJson.type)
    # for row in fromJson:
    #     print(row)
    # datastore = json.loads(fromJson)
    # newJson={}
    # for row in datastore:
    #     if row.item()[0] == "Email":
    #         newJson.append(row.item()[0], data)
    #
    return True

