import requests

def _send_request(endpoint):
    try:
        response = requests.get("https://example.com/api/v1/"+endpoint, timeout=4)
        return response.json()
    except requests.exceptions.ConnectionError:
        return {"result": False, "msg": "Cannot connect to server"}

def get_total_number_entry():
    try:
        return _send_request("entry/total_number")
    except Exception as e:
        print(e)

def get_total_number_exit():
    try:
        return _send_request("exit/total_number")
    except Exception as e:
        print(e)

def get_total_number_user():
    try:
        return _send_request("user/all/total_number")
    except Exception as e:
        print(e)

def get_total_number_ticket():
    try:
        return _send_request("ticket/all/total_number")
    except Exception as e:
        print(e)

