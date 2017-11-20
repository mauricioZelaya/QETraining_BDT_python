import requests

def get_conn(host, root_path, service, method, payload = None):
    """
    This method will set a connection to the endpoint, service and using the requested method.
    :param host: The host.
    :param root_path: The root_path.
    :param service: The method that will be tested.
    :param payload: Payload to send.
    :return: the response code
    """
    endpoint = host + root_path + service
    request = requested_method(endpoint, payload, method)
    return request.status_code

def get_response(host, root_path, service, method, payload = None):
    """
    This method execute a request and return the request in json format.
    :param host: Host.
    :param root_path: Root path.
    :param service: Service will be tested.
    :param method: Method will be used.
    :param payload: Payload to execute.
    :return: A request in json format.
    """
    endpoint = host + root_path + service
    request = requested_method(endpoint, payload, method)
    request = request.json()
    return request


def requested_method(endpoint, payload, method = "GET", headers = None):
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

def fill_payload(key, snippet = "snippet", videoId = None, q = None):
    """
    This method will fill the payload, if more attributes are required just add it at the end and set the
    initial value as None, for better call to this method set the name and the value in your call.
    :param key: API key for the user.
    :param snippet: required attribute for google API.
    :param videoId: The video Id.
    :param q: The video string that will be used to make a search
    :return: the payload in dictionary form
    """
    pay_load = {"part": snippet,
                "key": key,
                "videoId": videoId,
                "q": q}
    return pay_load
