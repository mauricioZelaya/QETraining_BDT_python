import requests

def get_conn(host, root_path, service, method, payload= None, headers= None):
    """
    This method will set a connection to the endpoint, service and using the requested method.
    :param host: The host.
    :param root_path: The root_path.
    :param service: The method that will be tested.
    :param payload: Payload to send.
    :return: the response code
    """

    endpoint = host + root_path + service
    request = requested_method(endpoint, payload, method, headers)
    return request.status_code


def requested_method(endpoint, payload, method, headers=None):
    """
    This method will return the request according the method sent
    :param endpoint: endpoint where we wil send the request
    :param payload: parameters required in the request
    :param method: method selected to perform the request
    :param headers: any additional header
    :return: None
    """
    if method == 'GET':
        return requests.get(endpoint, payload)
    elif method == 'POST':
        return requests.post(endpoint, payload, headers)
    elif method == 'PUT':
        return requests.put(endpoint, payload)
    elif method == 'DELETE':
        return requests.delete(endpoint)