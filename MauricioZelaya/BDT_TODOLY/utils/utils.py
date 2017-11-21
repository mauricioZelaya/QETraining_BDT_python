import requests

def get_conn(host, root_path, service, format, method = "GET", payload= None, headers= None, auth = None):
    """
    This method will set a connection to the endpoint, service and using the requested method.
    :param host: The host.
    :param root_path: The root_path.
    :param service: The method that will be tested.
    :param payload: Payload to send.
    :return: the response code
    """
    endpoint = host + root_path + service + format
    request = requested_method(endpoint, payload, method, headers, auth)
    return request.status_code

def get_response(host, root_path, service, format, method, payload = None, auth = None):
    """
    This method execute a request and return the request in json format.
    :param host: Host.
    :param root_path: Root path.
    :param service: Service will be tested.
    :param method: Method will be used.
    :param payload: Payload to execute.
    :return: A request in json format.
    """
    endpoint = host + root_path + service + format
    request = requested_method(endpoint, payload, method, auth)
    request = request.json()
    return request


def requested_method(endpoint, payload = None, method = "GET", headers = None, auth = None):
    """
    This method will return the request according the method sent
    :param endpoint: endpoint where we wil send the request
    :param payload: parameters required in the request
    :param method: method selected to perform the request
    :param headers: any additional header
    :return: None
    """
    if method == 'GET':
        return requests.get(endpoint, payload , auth = auth)
    elif method == 'POST':
        return requests.post(endpoint, payload)
    elif method == 'PUT':
        return requests.put(endpoint, payload)
    elif method == 'DELETE':
        return requests.delete(endpoint)

def fill_payload(format):

    return True

def fill_authorization_basic(user, pass_word):
    authorization = (user, pass_word)
    return authorization